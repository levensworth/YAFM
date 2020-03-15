pip install virtualenv
virtualenv -p python3.7 venv
echo 'Now listening for any changes ...'
. ./venv/bin/activate
python file-manager.py
