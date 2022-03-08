@ECHO OFF
echo BUILDING FOR RELEASE
cd ..
cd src
mkdir release
cd release
pip install pyinstaller
pyinstaller main-windows.py --distpath release --onefile -w -n CSD --windowed --add-data "logo.png" --add-data "tempfolder/"
powershell Compress-Archive -LiteralPath ".\CSD" -DestinationPath ".\CaveStoryDownloader.zip"
echo DONE BUILDIN, RELEASE IS IN \release LMAO
PAUSE
