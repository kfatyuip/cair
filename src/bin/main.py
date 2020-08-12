#!/usr/bin/env python3
# -*- coding: UTF-8

import os
import sys
import re
import platform
from bin import init
from bin.tools.functions import *

thisos = platform.system()

def fcimods(strs) :
    from bin import imods
    return imods.main(strs)

def funcplay(strs) :
    from bin.fun import funplay
    return funplay(strs)

def space(scan) :
    space = 0
    for i in scan :
        if i == " " :
            space += 1
    if space == len(scan) :
        return True
    else :
        return False

def main(scansc=init.dps,mode="",version=init.__version__,data=init.cair_start("")) :
    while True :
        scan = input(scansc)
        if scan == "cair" :
            main()
        elif scan == "exit" :
            init.cair_exit()
            sys.exit(0)
        elif scan.split(" ")[0] == "run" and len(scan.split(" ")) > 1 :
            os.system(scan.split(" ")[1])
        elif space(scan) == True :
            continue
        elif scan == "更新" or scan == "检查更新" :
            from bin.tools import check
            check.check(version,mi=data.get("MI"))
            continue
        elif scan == "cair日报" or scan == "日报" or scan == "头条" or scan == "新闻" :
            from bin.tools import news
            news.connect(mode)
            continue
        elif re.match("下载:",scan) :
            url = re.sub("下载:","",scan)
            from bin.mod import cwfd
            cwfd.download(url=url,file_path=os.path.basename(url))
            continue
        elif re.match("转巴祖木语:",scan) :
            cen = re.sub("转巴祖木语:","",scan)
            from bin.mod.bzm import zbzm
            print(zbzm.translate(cen))
            continue
        elif re.match("巴祖木语转:",scan) :
            cen = re.sub("巴祖木语转:","",scan)
            from bin.mod.bzm import bzmz
            print(bzmz.translate(cen))
            continue
        elif scan == "start server" or scan == "server" or scan == "start crsr" or scan == "crsr" :
            from bin.mod.crsr import server
            server.main()
        elif re.match("转叽叽喳喳语:",scan) :
            cen = re.sub("转叽叽喳喳语:","",scan)
            from bin.mod.jjzz import zjjzz
            print(zjjzz.translate(cen))
            continue
        elif re.match("叽叽喳喳语转:",scan) :
            cen = re.sub("叽叽喳喳语转:","",scan)
            from bin.mod.jjzz import jjzzz
            print(jjzzz.translate(cen))
            continue
        elif re.match("天气预报:",scan) :
            city = re.sub("天气预报:","",scan)
            from bin.mod import weather
            weather.main(city)
            continue
        elif scan == "bash" or scan == "sh" or scan == "zsh":
            if thisos == "Linux" :
                print("CAIR SHELL....")
                os.system(scan)
                continue
            else :
                output("在?什么时候换的Windows?")
        elif scan == "cmd" or scan == "command" :
            if thisos != "Linux" :
                print("CAIR CMD....")
                os.system(scan)
                continue
            else :
                output("在?什么时候换的Linux?")
        elif scan == "cls" and thisos == "Windows" :
            os.system(scan)
        elif scan == "clear" and thisos == "Linux" :
            os.system(scan)
        elif scan == "清屏" :
            os.system("cls" if thisos == "Windows" else "clear")
        elif funcplay(scan) :
            continue
        elif scan == "" :
            continue
        elif fcimods(scan) :
            continue
        else :
            from bin.fun import ask
            str = ask(scan)
            if str != "err" :
                print(str)
            else :
                print("日常听不懂:(")
