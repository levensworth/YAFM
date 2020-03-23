import settings
from injector import Injector
import os
import face_recognition
import logging

'''
PhotoInjector will be the class in charge of
imporved Photo management.
For it to work:
'''

class PhotoInjector(Injector):

    def __init__(self, logger, config=None):
        """
        For this particular injector you should pass a known images folder path for it to train the face recognition.
        Do remember to label the images with the name you want your folders.
        """
        super().__init__(logger, config=config)

        self.faces_name = {}
        self.faces_encoding = []
        path = config['known_path']
        index = 0
        for face_path in os.listdir(path):
            face_name = face_path.split('.')[0]
            image = face_recognition.load_image_file('{}/{}'.format(path, face_path))
            encodings = face_recognition.face_encodings(image)
            try:
                self.faces_encoding.append(encodings[0])
                self.faces_name[index] = face_name.capitalize()
                index += 1
                if len(encodings) > 1:
                    self.logger.warning("""image {} contains more than one face,
                    consider cropping it for performance improvements""".format(face_path))
            except IndexError:
                self.logger.warning('Could not recognize any faces from {}'.format(face_path))



    def process_file(self, path):
        unknown_picture = face_recognition.load_image_file(path)
        encodings = face_recognition.face_encodings(unknown_picture)
        for encoding in encodings:
            results = face_recognition.compare_faces(self.faces_encoding, encoding)
            for i in range(len(results)):
                if results[i]:
                    return '{}/{}'.format(self.config['sub_folder'], self.faces_name[i])

        return '{}'.format(self.config['sub_folder'])



if __name__ == '__main__':
    injector = PhotoInjector(logging, {'sub_folder': 'Image', 'types': ['png', 'jpeg', 'jpg'], 'known_path': './known'})
    new_path = injector.process_file('./unknown_me.jpg')
    print('new the path would be {}'.format(new_path))
