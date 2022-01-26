from guizero import *
from shutil import *

# Mac
mac_port_010 = "https://www.nakiwo.com/downloads/doukutsu0_1_0.dmg"
mac_port_009 = "https://www.nakiwo.com/downloads/doukutsu0_0_9.dmg"
mac_port_008 = "https://www.nakiwo.com/downloads/doukutsu0_0_8.dmg"
mac_port_007 = "https://www.nakiwo.com/downloads/doukutsu0_0_7.dmg"
mac_port_006 = "https://www.nakiwo.com/downloads/doukutsu0_0_6.dmg"
mac_prepatch_009 = "https://www.cavestory.org/downloads/cavestory_009_r1.dmg"
mac_spanish = "https://www.cavestory.org/downloads/cs_es_002.zip"
mac_prepatch_008 = "https://www.cavestory.org/downloads/CSMacPrepatched.dmg"
# Linux
linux_port = "https://www.cavestory.org/downloads/linuxdoukutsu-1.01.tar.bz2"
nx_engine_linux = "https://www.cavestory.org/downloads/LIN64-NXEngine-1.0.0.4-Rev-4.tar.gz"

def download():
    pass
app = App(title="Cave Story Downloader", height=600, width=500)

cavestorypic = Picture(app, image="src/logo.png")

choice = ButtonGroup(app, options=[["Mac Port 0.1.0 by Nakiwo", "MP10"], ["Mac Port 0.0.9 by Nakiwo", "MP09"], ["Mac Port 0.0.8 by Nakiwo", "MP08"], ["Mac Port 0.0.7 by Nakiwo", "MP07"]], selected="MP10")

app.display()