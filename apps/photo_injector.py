import settings
from injector import Injector
import os


'''
PhotoInjector will be the class in charge of
Photo management.
For it to work:
'''

class PhotoInjector(Injector):

    def process_file(self, path):
        return '{}'.format(self.config['sub_folder'])
