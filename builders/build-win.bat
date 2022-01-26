@ECHO OFF
ECHO BUILDING DEM CODE 4 WINDOWS LOL
ECHO REMEMBER DAT U NEED PYTHON ON DEM PATH LMAO
pip install pyinstaller
cd ..
cd src
mkdir compile
pyinstaller main-windows.py --onefile -w --name CaveStoryDL --distpath compile --add-data "logo-win.png" --add-data "tempfolder/"
ECHO DONE BUILDING LMAO
PAUSE
