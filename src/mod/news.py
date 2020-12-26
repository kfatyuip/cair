import sys
import json

def connect(mode="") :
    import requests
    from bin.mod import agent
    data = requests.get("https://crdtgzs.coding.net/p/file/d/cair/git/raw/master/info.json",headers={"User-Agent" : agent.ua("chrome")}).json()
    news = data["news"]
    if news != "" :
        print(news)

if __name__ == "__main__" :
    if len(sys.argv) >= 2 :
        connect(sys.argv[1])
    else :
        connect()
