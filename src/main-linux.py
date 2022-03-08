from guizero import *
import tarfile
from requests import *
from zipfile import ZipFile
from os import *

# Linux
linux_port = "https://www.cavestory.org/downloads/linuxdoukutsu-1.01.tar.bz2"
nx_engine_linux = "https://www.cavestory.org/downloads/LIN64-NXEngine-1.0.0.4-Rev-4.tar.gz"
dou_wine = "https://www.cavestory.org/downloads/cavestoryen.zip"

def download(url, filename):
    r = get(url, allow_redirects=True)
    open(filename, 'wb').write(r.content)

def dl2():
    if choice.value == "NX":
        download(nx_engine_linux, 'nxengine.tar.gz')
        nx_tar = tarfile.open('nxengine.tar.gz')
        nx_tar.extractall('./tempfolder')
        nx_tar.close()
        remove('nxengine.tar.gz')
        info("Successful", "NXEngine Linux has been successfully unpacked.")
    elif choice.value == "DouLinux":
        download(linux_port, 'dougnulinux.tar.bz2')
        dou_tar = tarfile.open('dougnulinux.tar.bz2')
        dou_tar.extractall('./tempfolder')
        dou_tar.close()
        remove('dougnulinux.tar.bz2')
        info("Successful", "Cave Story Linux Port has been successfully unpacked.")
    elif choice.value == "DouWine":
        download(dou_wine, 'cavestoryenwindows.zip')
        with ZipFile('cavestoryenwindows.zip', 'r') as DouZip:
            DouZip.extractall('tempfolder')
        remove('cavestoryenwindows.zip')
        info('Successful', 'Successfully unpacked Cave Story for Windows')

    
app = App(title="Cave Story Downloader", height=600, width=500)

cavestorypic = Picture(app, image="src/logo.png")

choice = ButtonGroup(app, options=[["NXEngine for Linux", "NX"], ["Cave Story Port", "DouLinux"], ["Cave Story English for Windows(for use in Wine)", "DouWine"]], selected="NX")
dl_button = PushButton(app, text="Download", command=dl2)

app.display()