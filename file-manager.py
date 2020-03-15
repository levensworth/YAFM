from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import time

"""
This script lets you organise your downloads folder into a separate folder with subfolders arranged by their type
and date
"""

SOURCE_FOLDER_PATH = '/Users/santiagobassani/Downloads'
DESTINATION_FOLDER = '/Users/santiagobassani/Downloads-Curated'

TYPED_FOLDERS = [
    {'sub_folder': 'Image', 'types': ['png', 'jpeg', 'jpg']},
    {'sub_folder':'Excel', 'types': ['xslx', 'csv', 'tsv', 'dat', 'data']},
    {'sub_folder': 'Documentas', 'types': ['txt', 'docx']},
    {'sub_folder': 'PDF', 'types': ['pdf']},
    {'sub_folder': 'Video', 'types': ['mp4']}
]
DEFAULT_FOLDER = 'Default'

class FileHandler(FileSystemEventHandler):
    """
    Event Handler for filesystem changes

    """
    def on_modified(self, event):
        for file_name in os.listdir(SOURCE_FOLDER_PATH):
            src = '{}/{}'.format(SOURCE_FOLDER_PATH, file_name)
            file_types = file_name.split('.')
            sub_folder = None
            for folder_type in TYPED_FOLDERS:
                if len(file_types) > 1 and file_types[1].lower() in folder_type["types"]:
                    sub_folder = folder_type['sub_folder']
            if sub_folder is None:
                sub_folder = DEFAULT_FOLDER

            try:
                os.mkdir('{}/{}'.format(DESTINATION_FOLDER, sub_folder))
            except Exception as e:
                pass
            new_src = '{}/{}/{}'.format(DESTINATION_FOLDER, sub_folder, file_name)

            os.rename(src, new_src)


event_handler = FileHandler()

observer = Observer()
observer.schedule(event_handler, SOURCE_FOLDER_PATH, recursive=True)
observer.start()

if __name__ == '__main__':
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt as e:
        observer.stop()

    observer.join()

