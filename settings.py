"""
This script let's you organise your downloads folder into a separate folder with subfolders arranged by their type
and date
"""

SOURCE_FOLDER_PATH = '/Users/santiagobassani/Downloads'
DESTINATION_FOLDER = '/Users/santiagobassani/Downloads-Curated'

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
    {'app': 'default_injector', 'config': {'sub_folder': 'Documents', 'types': ['txt', 'docx']}},
    {'app': 'default_injector', 'config': {'sub_folder': 'PDF', 'types': ['pdf']}},
    {'app': 'default_injector', 'config': {'sub_folder': 'SpreadSheets', 'types': ['xlsx', 'xls', 'csv', 'tsv','data']}},
    {'app': 'default_injector', 'config': {'sub_folder': 'CompressedFiles', 'types': ['zip', 'tar']}},
    {'app': 'default_injector', 'config': {'sub_folder': 'Apss', 'types': ['dmg', 'exe']}},
    {'app': 'default_injector', 'config': {'sub_folder': 'Programming', 'types': ['py', 'java', 'js', 'kt', 'sh', 'html']}},
    {'app': 'default_injector', 'config': {'sub_folder': 'Desgin', 'types': ['svg', 'ps']}}
    # This is an example use case. Please update path to match your desire folder
    # {'app': 'photo_injector', 'config': {'sub_folder': 'Image', 'known_path': './known' ,'types': ['png', 'jpeg', 'jpg']}}
]

