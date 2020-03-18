import settings
from injector import Injector
import os

'''
DocumentInjector will be the class in charge of
document management.
For it to work:
    - you will need to pass a path_vector containing all types accepted
'''

class DocumentInjector(Injector):

    def process_file(self, path):
        return '{}'.format(self.config['sub_folder'])

    def is_alive(self):
        print(self.types_vector)
