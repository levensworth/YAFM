import os

"""
Base model for any future injector
"""

class Injector():
    def __init__(self, logger, config=None):
        self.config = config if config is not None else {'sub_folder': 'Default', 'types': []}
        self.logger = logger

    def is_alive(self):
        print('i"m alive!')

    def get_extensions(self):
        '''
        returns all extensions supported by the class
        '''
        return self.types_vector['types']

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
        """
        This method should return the path under the base folder where the file should be moved to.
        """
        raise NotImplementedError()
