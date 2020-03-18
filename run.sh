echo 'Installing virtualenv'
pip install virtualenv
echo 'creating a venv'
virtualenv -p python3.7 venv
echo 'activating venv'
. ./venv/bin/activate
echo 'installing requirements.txt'
pip install -r requirements.txt
echo 'start listener ...'
python file_manager.py
