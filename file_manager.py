import settings
from injection_manager import InjectionManager
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import time
from settings import DEFAULT_FOLDER, SOURCE_FOLDER_PATH, TYPED_FOLDERS, DESTINATION_FOLDER
import logging


class FileHandler(FileSystemEventHandler):

    def __init__(self, logger, depency_manager):
        super().__init__()
        self.logger = logger
        self.dependency_manager = depency_manager

    """
    Event Handler for filesystem changes
    """
    def on_modified(self, event):
        for file_name in os.listdir(SOURCE_FOLDER_PATH):
            src = '{}/{}'.format(SOURCE_FOLDER_PATH, file_name)
            move = True
            try:
                file_type = file_name.split('.')[-1]
                injector = self.dependency_manager.get_injector(file_type)
                sub_folder = injector.process(src)
                os.mkdir('{}/{}'.format(DESTINATION_FOLDER, sub_folder))
            except IndexError:
                # it's folder or an unknown file
                self.logger.warning("file {} can't be processed, please each file must have an extention".format(file_name))
                move = False
            except NotImplementedError:
                self.logger.warning('{}: this extension has no parser yet.'.format(file_name))
                move = False
            except FileExistsError:
                pass
            except FileNotFoundError:
                # mkdir failed
                self.logger.error('destination folder does not exists')
            except Exception:
                self.logger.warning('something went wrong, please go to the repo and tell us about it')

            if move:
                new_src = '{}/{}/{}'.format(DESTINATION_FOLDER, sub_folder, file_name)
                os.rename(src, new_src)


if __name__ == '__main__':
    while True:
        try:
            # start dependency manager
            dependency_manager = InjectionManager(settings.APPS, logging)
            # start event handler and inject dp_manager
            event_handler = FileHandler(logging, dependency_manager)
            # watchdog_observer
            observer = Observer()
            observer.schedule(event_handler, SOURCE_FOLDER_PATH, recursive=True)
            observer.start()
            while True:
                time.sleep(10)
        except KeyboardInterrupt as e:
            observer.stop()
            exit()
        except Exception as e:
            observer.stop()

    observer.join()
