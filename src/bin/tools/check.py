#!/usr/bin/env python3
# -*- coding : UTF-8 -*-

import json
from bin.tools.functions import *

url = "https://crdtgzs.rthe.xyz/cair/files/info.json"

def strfloat(s) :
    s = str(s)
    if s.find(".") != -1 and s.find(".") != 0 :
        b = s.split(".")
        if b[0].isdigit() and b[1].isdigit() :
            return b

def check(v,mi=url) :
    import requests
    from bin.mod import agent
    if mi == None :
        mi = url
    msg = requests.get(mi,headers={"User-Agent": agent.ua("chrome")})
    data = msg.json()
    if strfloat(data["NV"])[0] >= strfloat(v)[0] and strfloat(data["NV"])[1] > strfloat(v)[1] :
        output("最新版本:%s 当前版本%s" % (str(data["NV"]),str(v)))
        output("有新版本啦!快去官网下载吧")
    else :
        output("当前已是最新版本!")
