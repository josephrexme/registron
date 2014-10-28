set PIP=c:\python27\PyInstaller\
python %PIP%Makespec.py --onefile --console --upx --tk registron.py
python %PIP%Build.py registron.spec
