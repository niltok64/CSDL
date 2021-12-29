from requests import *
from guizero import *
from zipfile import *
from tempfile import mkdtemp
import os

doukutsu_url = "https://studiopixel.jp/binaries/dou_1006.zip"
cavestory_enpatch = "https://aeongenesis.net/download/cavestory"
cavestory_prepatch_en = "https://www.cavestory.org/downloads/cavestoryen.zip"

tempfolder = mkdtemp()

def download():
    if version.value == "DC":
        dou = get(doukutsu_url, allow_redirects=True)
        open('doukutsu_monogatari.zip', 'wb').write(dou.content)
        with ZipFile("doukutsu_monogatari.zip", "r") as zip_ref:
            zip_ref.extractall("tempfolder")
        info("Finished", "Doukutsu Monogatari has been extracted in the temp folder")
        os.remove("doukutsu_monogatari.zip")
    elif version.value == "EP":
        enp = get(cavestory_enpatch, allow_redirects=True)
        open('en_patch.zip', 'wb').write(enp.content)
        with ZipFile("en_patch.zip", "r") as zip_ref:
            zip_ref.extractall("tempfolder")
        info("Finished", "The patch has been extracted in the temp folder")
        os.remove("en_patch.zip")
    else:
        prepatch = get(cavestory_prepatch_en, allow_redirects=True)
        open('cavestory.zip', 'wb').write(prepatch.content)
        with ZipFile("cavestory.zip", "r") as zip_ref:
            zip_ref.extractall("tempfolder")
        info("Finished", "Cave Story has been extracted in the temp folder")
        os.remove("cavestory.zip")

app = App(title="Cave Story Downloader")

cavestorypic = Picture(app, image="Cave_Story_logo.png", width=200, height=200)
version = ButtonGroup(app, options=[["Doukutsu Monogatari", "DC"], ["Cave Story English Patch", "EP"], ["Cave Story English Pre-Patched", "PP"]], selected="DC")
download_button = PushButton(app, command=download, text="Download")

app.display()