import settings
from injector import Injector
import os

'''
ExcelInjector will be the class in charge of
pdf management.
For it to work:
    - you will need to pass a path_vector containing all types accepted
'''

class ExcelInjector(Injector):

    def process_file(self, path):
        return '{}'.format(self.config['sub_folder'])

