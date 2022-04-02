from requests import *
from guizero import *
from zipfile import *
from tempfile import mkdtemp
import os
import patoolib
import py7zr

doukutsu_url = "https://studiopixel.jp/binaries/dou_1006.zip"
cavestory_enpatch = "https://aeongenesis.net/download/cavestory"
cavestory_prepatch_en = "https://www.cavestory.org/downloads/cavestoryen.zip"
deluxepack_updated = "https://www.cavestory.org/downloads/Cave_Story_Deluxe.exe"
deluxepack_old = "https://www.cavestory.org/downloads/Cave_Story_Deluxe_old.exe"
# translations
brazilian_portuguese = "https://www.cavestory.org/downloads/Cave_Story_pt-BR_v1.0.rar"
chinese_simplified = "https://pawism.com/sp/doukutsu/pub/dou_sc102.zip"
chinese_traditional = "https://www.cavestory.org/downloads/dou_chinese.exe"
dutch = "https://cavestorynl.weebly.com/uploads/4/8/5/2/48528295/cavestorynl29-9-2017.zip"
french = "https://www.cavestory.org/downloads/cave_story_fr_1_11.zip"
german_LB = "https://www.cavestory.org/downloads/Cave%20Story%20DE%203V%20Installer%20(LB%20Produkt).exe"
italian = "https://www.cavestory.org/downloads/Cave_Story_Italian_v2.0.zip"
korean = "https://download843.mediafire.com/umno3dfsiedg/fok0mwj47aj9hft/cavestory_k.7z"
lithuanian = "https://www.cavestory.org/downloads/cavestor.rar"
polish = "https://www.cavestory.org/downloads/cavestorypl.zip"
portuguese = "https://www.cavestory.org/downloads/Cave_Story_pt_PT.7z"
russian = "https://www.cavestory.org/downloads/Cave_Story_v1.006_RUS.rar"
spanish = "https://www.cavestory.org/downloads/cave.rar"

tempfolder = mkdtemp()

def open_window():
    window.show()

def close_window():
    window.hide()

def download():
    if version.value == "DC":
        dou = get(doukutsu_url, allow_redirects=True)
        open('doukutsu_monogatari.zip', 'wb').write(dou.content)
        with ZipFile("doukutsu_monogatari.zip", "r") as zip_ref:
            zip_ref.extractall("tempfolder")
        os.remove("doukutsu_monogatari.zip")
        info("Finished", "Doukutsu Monogatari has been extracted in the temp folder")
    elif version.value == "EP":
        enp = get(cavestory_enpatch, allow_redirects=True)
        open('en_patch.zip', 'wb').write(enp.content)
        with ZipFile("en_patch.zip", "r") as zip_ref:
            zip_ref.extractall("tempfolder")
        os.remove("en_patch.zip")
        info("Finished", "The patch has been extracted in the temp folder")
    else:
        prepatch = get(cavestory_prepatch_en, allow_redirects=True)
        open('cavestory.zip', 'wb').write(prepatch.content)
        with ZipFile("cavestory.zip", "r") as zip_ref:
            zip_ref.extractall("tempfolder")
        os.remove("cavestory.zip")
        info("Finished", "Cave Story has been extracted in the temp folder")

def download_dx():
    if deluxeversion.value == "DP":
        dlxupd = get(deluxepack_updated, allow_redirects=True)
        open('cavestorydx.exe', 'wb').write(dlxupd.content)
        info("Finished", "The Cave Story Deluxe EXE has finished downloading")
    else:
        dlxold = get(deluxepack_old, allow_redirects=True)
        open('cavestorydx_old.exe', 'wb').write(dlxold.content)
        info("Finished", "The old Cave Story Deluxe EXE has finished downloading")

def download_lang():
    if patch_choice.value == "BPE":
        bpe = get(brazilian_portuguese, allow_redirects=True)
        open('doukutsu_brazil.rar', 'wb').write(bpe.content)
        patoolib.extract_archive("doukutsu_brazil.rar", outdir="tempfolder")
        os.remove("doukutsu_brazil.rar")
        info("Finished", "Cave Story in Brazilian Portuguese has finished downloading")
    elif patch_choice.value == "CS":
        cs = get(chinese_simplified, allow_redirects=True)
        open('doukutsu_chinese_simplified.zip', 'wb').write(cs.content)
        with ZipFile("doukutsu_chinese_simplified.zip", "r") as zip_ref:
            zip_ref.extractall("tempfolder")
        os.remove("doukutsu_chinese_simplified.zip")
        info("Finished", "Cave Story in Simplified Chinese has finished downloading")
    elif patch_choice.value == "D":
        dutchpatch = get(dutch, allow_redirects=True)
        open('doukutsu_dutch.zip', 'wb').write(dutchpatch.content)
        with ZipFile("doukutsu_dutch.zip", "r") as zip_ref:
            zip_ref.extractall("tempfolder")
        os.remove("doukutsu_dutch.zip")
        info("Finished", "Cave Story in Dutch has finished downloading")
    elif patch_choice.value == "Fr":
        fr = get(french, allow_redirects=True)
        open("doukutsu_francais.zip", "wb").write(fr.content)
        with ZipFile("doukutsu_francais.zip", "r") as zip_ref:
            zip_ref.extractall("tempfolder")
        os.remove("doukutsu_francais.zip")
        info("Finished", "Cave Story in French has finished downloading")
    elif patch_choice.value == "G":
        ger = get(german_LB, allow_redirects=True)
        open("doukutsu_deutsch.exe", "wb").write(ger.content)
        info("Finished", "Cave Story in German has finished downloading")
    elif patch_choice.value == "It":
        ity = get(italian, allow_redirects=True)
        open("doukutsu_italiano.zip", "wb").write(ity.content)
        with ZipFile("doukutsu_italiano.zip", "r") as zip_ref:
            zip_ref.extractall("tempfolder")
        os.remove("doukutsu_italiano.zip")
        info("Finished", "Cave Story in Italian has finished downloading")
    elif patch_choice.value == "K":
        kor = get(korean, allow_redirects=True)
        open("doukutsu_korean.7z", "wb").write(kor.content)
        with py7zr.SevenZipFile("doukutsu_korean.7z", mode="r") as z:
            z.extractall()
        os.remove("doukutsu_korean.7z")
        info("Finished", "Cave Story in Korean has finished downloading")
    elif patch_choice.value == "L":
        lith = get(lithuanian, allow_redirects=True)
        open("doukutsu_lithuanian.rar", "wb").write(lith.content)
        patoolib.extract_archive("doukutsu_lithuanian.rar", outdir="tempfolder")
        os.remove("doukutsu_lithuanian.rar")
        info("Finished", "Cave Story in Lithuanian has finished downloading")
    elif patch_choice.value == "Po":
        pol = get(polish, allow_redirects=True)
        open("doukutsu_polska.zip", "wb").write(pol.content)
        with ZipFile("doukutsu_polska.zip", "r") as zip_ref:
            zip_ref.extractall("tempfolder")
        os.remove("doukutsu_polska.zip")
        info("Finished", "Cave Story in Polish has finished downloading")
    elif patch_choice.value == "Por":
        por = get(portuguese, allow_redirects=True)
        open("doukutsu_portuguese.7z", "wb").write(por.content)
        with py7zr.SevenZipFile('doukutsu_portuguese.7z', mode='r') as z:
            z.extractall()
        os.remove("doukutsu_portuguese.7z")
        info("Finished", "Cave Story in Portuguese has finished downloading")
    elif patch_choice.value == "Rus":
        rus = get(russian, allow_redirects=True)
        open("doukutsu_russian.rar", "wb").write(rus.content)
        patoolib.extract_archive("doukutsu_russian.rar", outdir="tempfolder")
        os.remove("doukutsu_russian.rar")
        info("Finished", "Cave Story in Russian has finished downloading")
    else:
        spa = get(spanish, allow_redirects=True)
        open("doukutsu_spanish.rar", "wb").write(spa.content)
        patoolib.extract_archive("doukutsu_spanish.rar", outdir="tempfolder")
        os.remove("doukutsu_spanish.rar")
        info("Finished", "Cave Story in Spanish has finished downloading")


app = App(title="Cave Story Downloader", height=620, width=500)
window = Window(app, title="Language Patch options", height=550, width=500)
close_window()


# app
normal_text = Text(app, text="Standard version")
version = ButtonGroup(app, options=[["Doukutsu Monogatari", "DC"], ["Cave Story English Patch", "EP"], ["Cave Story English Pre-Patched", "PP"]], selected="DC")
download_button = PushButton(app, command=download, text="Download and Extract")
deluxepack_text = Text(app, text="Deluxe pack")
deluxeversion = ButtonGroup(app, options=[["Cave Story Deluxe Pack", "DP"], ["Old Cave Story Deluxe Pack", "ODP"]], selected="DP")
download_button_dx = PushButton(app, command=download_dx, text="Download Deluxe Pack")
lang_option_button = PushButton(app, command=open_window, text="Language patch options")

# window
patch_choice = ButtonGroup(window, options=[["Simplified Chinese", "CS"], ["Dutch", "D"], ["French", "Fr"], ["German", "G"], ["Italian", "It"], ["Korean", "K"], ["Polish", "Po"], ["Portuguese", "Por"]], selected="CS")
download_lang_button = PushButton(window, command=download_lang, text="Download")
close = PushButton(window, command=close_window, text="Close")

app.display()
