"""
This script let's you organise your downloads folder into a separate folder with subfolders arranged by their type
and date
"""

SOURCE_FOLDER_PATH = '/Users/sbassani/Downloads'
DESTINATION_FOLDER = '/Users/sbassani/Downloads-Curated'

# deprecated
TYPED_FOLDERS = [
    {'sub_folder': 'Image', 'types': ['png', 'jpeg', 'jpg']},
    {'sub_folder':'Excel', 'types': ['xslx', 'csv', 'tsv', 'dat', 'data']},
    {'sub_folder': 'Documentas', 'types': ['txt', 'docx']},
    {'sub_folder': 'PDF', 'types': ['pdf']},
    {'sub_folder': 'Video', 'types': ['mp4']}
]

DEFAULT_FOLDER = 'Default'

APPS_BASE_PATH = 'apps'

APPS = [
    {'app': 'document_injector', 'config': {'sub_folder': 'Documents', 'types': ['txt', 'docx']}},
    {'app': 'pdf_injector', 'config': {'sub_folder': 'PDF', 'types': ['pdf']}},
    {'app': 'excel_injector', 'config': {'sub_folder': 'SpreadSheets', 'types': ['xlsx', 'xls', 'csv', 'tsv','data']}},
    {'app': 'zip_injector', 'config': {'sub_folder': 'CompressedFiles', 'types': ['zip', 'tar']}},
    {'app': 'photo_injector', 'config': {'sub_folder': 'Image', 'types': ['png', 'jpeg', 'jpg']}}
]
