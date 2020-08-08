import json
import os
import platform

bq = "/" if platform.system() == "Linux" else "\\"

def getargv(bq,sets="data" + bq + "settings.json") :
    if os.path.isfile(sets) :
        with open(sets,mode="r") as f :
            read = f.read()
        data = json.loads(read)
        return data.get(bq)
    else :
        return None

def getinfo(jn="data" + bq + "settings.json") :
    if os.path.isfile(jn) :
        return json.loads(jn)
    else :
        return None
