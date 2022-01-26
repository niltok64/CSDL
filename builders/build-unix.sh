#!/bin/sh
echo "BUILDING DEM CODE 4 UNIX LOL"
echo REMEMBER DAT U NEED PYTHON ON DEM PATH LMAO
pip install pyinstaller
cd ..
cd src
mkdir compile
pyinstaller main-unix.py --onefile -w --name CaveStoryDL --distpath compile --add-data "logo.png" --add-data "tempfolder/"
echo "DONE BUILDING LMAO"
