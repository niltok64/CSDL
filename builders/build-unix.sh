#!/bin/sh
echo BUILDING DEM CODE 4 UNIX LOL
echo REMEMBER DAT U NEED PYTHON ON DEM PATH LMAO
pip install pyinstaller
cd ..
mkdir compile
pyinstaller main.py --onefile -w --name CaveStoryDL --distpath compile
echo DONE BUILDING LMAO
echo REMEMBER TO PUT DA LOGO IN COMPILE FOLDER AND FROLIC YOOO
