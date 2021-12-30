from requests import *
from guizero import *
from zipfile import *
from tempfile import mkdtemp
import os

doukutsu_url = "https://studiopixel.jp/binaries/dou_1006.zip"
cavestory_enpatch = "https://aeongenesis.net/download/cavestory"
cavestory_prepatch_en = "https://www.cavestory.org/downloads/cavestoryen.zip"
deluxepack_updated = "https://www.cavestory.org/downloads/Cave_Story_Deluxe.exe"
deluxepack_old = "https://www.cavestory.org/downloads/Cave_Story_Deluxe_old.exe"

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

def download_dx():
    if deluxeversion.value == "DP":
        dlxupd = get(deluxepack_updated, allow_redirects=True)
        open('cavestorydx.exe', 'wb').write(dlxupd.content)
        info("Finished", "The Cave Story Deluxe EXE has finished downloading")
    else:
        dlxold = get(deluxepack_old, allow_redirects=True)
        open('cavestorydx_old.exe', 'wb').write(dlxold.content)
        info("Finished", "The old Cave Story Deluxe EXE has finished downloading")

app = App(title="Cave Story Downloader", height=550, width=500)

cavestorypic = Picture(app, image="logo.png")

normal_text = Text(app, text="Standard version")
version = ButtonGroup(app, options=[["Doukutsu Monogatari", "DC"], ["Cave Story English Patch", "EP"], ["Cave Story English Pre-Patched", "PP"]], selected="DC")
download_button = PushButton(app, command=download, text="Download and Extract")
deluxepack_text = Text(app, text="Deluxe pack")
deluxeversion = ButtonGroup(app, options=[["Cave Story Deluxe Pack", "DP"], ["Old Cave Story Deluxe Pack", "ODP"]], selected="DP")
download_button_dx = PushButton(app, command=download_dx, text="Download Deluxe Pack")

app.display()