import json
import requests
from bin.mod import agent

def i_to_you(s) :
    result = ""
    for i in str(s) :
        if i == "我" :
            result += "你"
        else :
            if i == "你" :
                result += "我"
            else :
                result += i
    return result

def funplay(s) :
    import re
    import platform
    from bin.fileos import getargv
    from os.path import isfile
    fg = "/" if platform.system() == "Linux" else "\\"
    ok = True
    err = False
    if isfile("files" + fg + "ck.json") :
        r = getargv(s,"files" + fg + "ck.json")
        if r != None :
            print(r)
            return ok
        else :
            return err
    else :
        return err

def ask(s) :
    try :
        get = requests.get("http://muyu.dsw20.com/api/lt.php?msg=%s" % s,headers = { "User-Agent": agent.ua("chrome")}).text
        return get
    except :
        return "err"
