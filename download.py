from requests import *
from guizero import *

doukutsu_url = "https://studiopixel.jp/binaries/dou_1006.zip"
cavestory_enpatch = "https://aeongenesis.net/download/cavestory"
cavestory_prepatch_en = "https://www.cavestory.org/downloads/cavestoryen.zip"

def download():
    if version.value == "DC":
        dou = get(doukutsu_url, allow_redirects=True)
        open('doukutsu_monogatari.zip', 'wb').write(dou.content)
        info("Finished", "Doukutsu Monogatari has finished downloading")
    elif version.value == "EP":
        enp = get(cavestory_enpatch, allow_redirects=True)
        open('en_patch.zip', 'wb').write(enp.content)
        info("Finished", "The patch has finished downloading")
    else:
        prepatch = get(cavestory_prepatch_en, allow_redirects=True)
        open('cavestory.zip', 'wb').write(prepatch.content)
        info("Finished", "Cave Story has finished downloading")

app = App(title="Cave Story Downloader")

cavestorypic = Picture(app, image="Cave_Story_logo.png", width=200, height=200)
version = ButtonGroup(app, options=[["Doukutsu Monogatari", "DC"], ["Cave Story English Patch", "EP"], ["Cave Story English Pre-Patched", "PP"]], selected="DC")
download_button = PushButton(app, command=download, text="Download")

app.display()