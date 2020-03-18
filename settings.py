"""
This script let's you organise your downloads folder into a separate folder with subfolders arranged by their type
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

APPS = [
    {'app': 'document_injector', 'config': {'sub_folder': 'Documentas', 'types': ['txt', 'docx']}},
    {'app': 'pdf_injector', 'config': {'sub_folder': 'PDF', 'types': ['pdf']}}
]
