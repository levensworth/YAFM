import os

class Injector():
    def __init__(self, config=None):
        self.config = config if config is not None else {'sub_folder': 'Default', 'types': []}

    def is_alive(self):
        print('i"m alive!')

    def get_extensions(self):
        '''
        returns all extensions supported by the class
        '''

        raise NotImplementedError()

    def process(self, path):
        '''
        Process a file domain specific. if its a folder it should just go with the default
        return a path
        '''
        if os.path.isfile(path):
            return self.process_file(path)
        else:
            raise NotImplementedError()

    def process_file(self, path):
        raise NotImplementedError()
