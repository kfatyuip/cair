import json
import requests
from bin.mod import agent

def main(city) :
    url = "http://wthrcdn.etouch.cn/weather_mini?city=%s" % city
    jsong = json.loads(requests.get(url,agent.ua("chrome")).text)
    data = jsong["data"]["forecast"][0]
    print("日期:",data["date"])
    print("温度:",data["high"],data["low"])
    print("风力:",data["fengli"])
    print("风向:",data["fengxiang"])
    print("类型:",data["type"])
    print(jsong["data"]["ganmao"])

if __name__ == "__main__" :
    main("北京")
