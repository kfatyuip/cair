import json

def getargv(bq,sets="settings.json") :
    with open(sets,mode="r") as f :
        read = f.read()
    data = json.loads(read)
    return data.get(bq)

def getinfo(jn="settings.json") :
    return json.loads(jn)
