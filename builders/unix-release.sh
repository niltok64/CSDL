#!/bin/sh
echo "BUILDING"
cd ..
cd src
mkdir release-unix
pyinstaller main-unix.py --onefile -w -n CSD --distpath release-unix --add-data icon.png --add-data "tempfolder/"
cd release-unix
zip -r9 "CaveStoryDownloader-Unix" "CSD/"
echo "DONE BUILDIN, RELEASE IN /release LMAO"
