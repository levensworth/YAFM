import settings
import os
import importlib
import logging
import inspect
from injector import Injector
import types

"""
Injector dependecy manager
"""

class InjectionManager():
    def __init__(self, apps, logger):
        ''' Inject each extension manager '''
        self.logger = logger
        self.injectors = []

        for app in apps:

            path = app['app']
            try:
                # https://stackoverflow.com/questions/49434118/python-how-to-create-a-class-object-using-importlib
                mod = importlib.import_module('{}.{}'.format(settings.APPS_BASE_PATH, path),)

                module_classes = inspect.getmembers(mod, inspect.isclass)
                for class_implementation in module_classes:
                    if not is_injector(class_implementation[1]):
                        module_classes.remove(class_implementation)
                instance = module_classes[0][1]
                instance = instance(self.logger, app['config'])
                self.injectors.append(instance)

            except  ImportError:
                self.logger.warning('''Error getting
                {} module. Please, remember to name the file as the Class'''.format(path))

    def get_injector(self, extension):
        for injector in self.injectors:
            if extension.lower() in injector.config['types']:
                return injector
        raise NotImplementedError


def is_injector(object):
    check_subclass = issubclass(object, Injector)
    check_class = not (object == Injector)
    return check_subclass and check_class
