#!/bin/sh
echo "BUILDING"
cd ..
cd src
mkdir release-unix
pyinstaller main-linux.py --onefile -w -n CSD --distpath release-unix --add-data icon.png --add-data "tempfolder/"
cd release-unix
zip -r9 "CaveStoryDownloader-Linux" "CSD/"
echo "DONE BUILDIN, RELEASE IN /release LMAO"
