# /usr/local/bin/
source venv/bin/activate 
pyinstaller amber.py --onefile
sudo cp dist/amber /usr/local/bin/