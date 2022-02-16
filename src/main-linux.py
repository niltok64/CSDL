from guizero import *
from shutil import *

# Linux
linux_port = "https://www.cavestory.org/downloads/linuxdoukutsu-1.01.tar.bz2"
nx_engine_linux = "https://www.cavestory.org/downloads/LIN64-NXEngine-1.0.0.4-Rev-4.tar.gz"

def download():
    pass
app = App(title="Cave Story Downloader", height=600, width=500)

cavestorypic = Picture(app, image="src/logo.png")

choice = ButtonGroup(app, options=[["NXEngine for Linux", "NX"], ["Cave Story Port", "DouLinux"]], selected="NX")

app.display()