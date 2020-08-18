#!/usr/bin/env python3
# -*- coding : UTF-8 -*-

import json
from bin import ids

url = "https://crdtgzs.coding.net/p/file/d/cair/git/raw/master/info.json"

def check(v,mi=url) :
    import requests
    from bin.mod import agent
    if mi == None :
        mi = url
    msg = requests.get(mi,headers={"User-Agent": agent.ua("chrome")})
    data = msg.json()
    if  str(data["NV"]) != str(v) :
        ids.output("最新版本:%s 当前版本%s" % (str(data["NV"]),str(v)))
        ids.output("有新版本啦!快去官网下载吧")
    else :
        ids.output("当前已是最新版本!")
