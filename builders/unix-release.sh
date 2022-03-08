#!/bin/sh
echo "BUILDING"
cd ..
cd src
mkdir release-unix
cd release-unix
pyinstaller main-unix.py --onefile -w -n CSD --distpath release-unix --add-data "logo.png" --add-data "tempfolder/"
zip -r9 "CaveStoryDownloader-Unix" "CSD/"
echo "DONE BUILDIN, RELEASE IN /release LMAO"
