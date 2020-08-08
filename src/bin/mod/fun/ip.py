import json
import requests

def getip() :
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"}
    data = json.loads(requests.get("http://ip-api.com/json/",headers=headers).text)
    return "ip:" + data["query"] + "\n" + "regionName:" + data["regionName"] + "\n" + "city:" + data["city"]

if __name__ == "__main__" :
    getip()
