#!/bin/sh
echo BUILDING
cd ..
mkdir release-unix
pyinstaller main.py --onefile -w -n CSD --distpath release-unix --add-data icon.png
cd release-unix
zip -r9 "CaveStoryDownloader-Linux" "CSD/"
echo FINISHED BUILDING, RELEASE IN \release FOLDER LMAO
