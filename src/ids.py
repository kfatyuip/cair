import os
import sys
import platform
import json
import fileos

bq = "\\" if platform.system() == "Windows" else "/"

__author__ = "kfatyuip"
__version__ = "3.0"
__vt__ = "Stable"
__it__ = "Standard"

setjson = "data" + bq + "settings.json"
color = False
thisos = platform.system()
if thisos != "Windows" :
    dps = "Root@CAIR:#"
else :
    dps = "Admin@CAIR:#"
    
if __it__ == "Standard" :
    name = "CAIR"
else :
    name = __it__

#if not os.path.exists("lib"):
#      os.makedirs("lib")

def output(s) :
    print("%s:|%s" % (name,s))


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
                if thisos != "Windows" :
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
        if thisos != "Windows" :
            print("\033[0m",end="")
        else :
            os.system("color")
