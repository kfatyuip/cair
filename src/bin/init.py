import os
import sys
import platform
import json
from bin import fileos

sys.path.append(os.getcwd() + "/bin/pymod/")

__author__ = "kfatyuip"
__version__ = "2.8"
__vt__ = "Stable"
__it__ = "Standard"

bq = "/" if platform.system() == "Linux" else "\\"
setjson = "data" + bq + "settings.json"
color = False
thisos = platform.system()
if thisos == "Linux" :
    dps = "Root@CAIR:#"
else :
    dps = "Admin@CAIR:#"

def path(p) :
    import re
    sys.path.append(re.sub("(\w)+.py","",p) + "bin" + bq + "pymod" + bq)
def cair_start(mode=None) :
    global color
    zd = {}
    try :
        if os.path.exists(setjson) :
            if fileos.getargv("color") :
                color = True
                if thisos == "Linux" :
                    print("\033[32m",end="")
                else :
                    os.system("color a")
            if fileos.getargv("welcome") != "" and fileos.getargv("welcome") != 0 and fileos.getargv("welcome") != None :
                if mode == None :
                    print(fileos.getargv("welcome"))
                zd.update({"welcome" : True})
            else :
                zd.update({"welcome" : False})
            if fileos.getargv("MI") != "" :
                zd.update({"MI" : fileos.getargv("MI")})
        return zd
    except KeyError:
        return -1

def cair_exit() :
    global color
    if color :
        if thisos == "Linux" :
            print("\033[0m",end="")
        else :
            os.system("color")
