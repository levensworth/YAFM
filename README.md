# Yet Another File Manager
If you have a mac, your Donwloads folder is a mess.
This script comes to save you.
This module was intended to be an extensible implementation for anyone to introduce changes on runtime

## How it works?:
1. open `settings.py` with your text editor of choice and follow the instructions below.
2. `SOURCE_FOLDER_PATH = ...` should point to the full path to the folder where changes may occur.
3. `DESTINATION_FOLDER= ...` should point to the full path of the root folder where the (now clssified) files will be.
4. Run `chmod u+x run.sh` this just allow your shell to execute the file `run.sh`
5. Run `./run.sh` this will create a virtualenv and download the necessary requirements, after that start watching for your folder.

## How to handle new extensions?
If you want to make a new handler for an extension which is currently not implemented or just pourly handle you can!
YAFM was build with extension as a core principle. 
1. Create a new python file inside the module `apps` (eg: `example_handler.py`).
2. Create your handler class, be sure to extend `Injector`. For that, `from injector import Injector`
3. Your newly created handler must implement `process_file(self, path)` which must return a string representing the sub path under `DESTINATION_FOLDER` where the file should be moved to.
4. In `settings.py` inside the `APPS = [...]` include a new row as `{'app': 'example_handler', 'config': {'sub_folder': 'Example', 'types': ['pdf']}}`
    - The `'app'` attribute reference the file name.
    - The  `'sub_folder'` attribute reference the Subfolder to be generated under the  `DESTINATION_FOLDER `. This will be consider the base direction for any file given to this handler, but inside you can just go as deep as you want!
    - The `'types'` attribute represents an array of all accepted types for this module. Make sure no two apps clash with the types they accept as we cannot asure you which one will process each file.

5. Now you can use `PhotoInjector` for image classification of your downloads.
    - Inside `settings.py` you'll add an entry for `APPS = [...]`.
    - The new entry should look like this:
        `{'app': 'photo_injector', 'config': {'sub_folder': 'Image', 'known_path': 'path/to/folder' ,'types': ['png', 'jpeg', 'jpg']}}`
    - For this injector to work you'll specify a folder path in `known_path` containing one image for each person you want to 
        classify. Each photo should contain the person's face looking forward (please, this is crucial for performance and accuracy). The name of each photo will be used to create each folder inside the `DESTINATION_FOLDER`.

## Work of art in progress.
Please be kind, this is a side project. If you have any suggestions or want to contribute, i encurage you to do so!.

## Depdenceies:
- python3
- virtualenv

email: sanitago.bassani96@gmail.com
