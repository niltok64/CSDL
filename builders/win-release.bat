@ECHO OFF
echo BUILDING FOR RELEASE
cd ..
mkdir release
pip install pyinstaller
pyinstaller main.py --distpath release --onefile -w -n CSD --windowed --add-data "icon.png"
cd release
powershell Compress-Archive -LiteralPath ".\CSD" -DestinationPath ".\CaveStoryDownloader.zip"
echo DONE BUILDIN, RELEASE IS IN \release LMAO
PAUSE
