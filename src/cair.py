#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os
import sys
import platform
import ids
import imods

ids.path(sys.argv[0])
__version__ = ids.__version__
this_os = platform.system()
dps = ids.dps

dwf = True
status = ids.cair_start()
if status.get("welcome") == True :
    dwf = False
MI = status.get("MI")
data = status

def output(strs) :
    print("CAIR:|" + str(strs))

def welcome() :
    print("欢迎使用CAIR人工智能机器人")
    print("操作系统: %s" % platform.platform())
    print("版本: %s" % ids.__version__,"类型: %s版" % ids.__vt__,"发行版本: %s" % ids.__it__)
    print("版权所有: CRDT Studio","开发者: %s" % ids.__author__)

start_out = "-" * 30
thisos = platform.system()

def main(scansc=ids.dps,mode="",version=ids.__version__,data=ids.cair_start("")) :  imods.main(scansc)

def start(mode="main",debug=None) :
    if debug != None :
        if debug == "debug" :
            if dwf :
                welcome()
            output("##开发者DEBUG模式已启动##")
            print(start_out)
            main(dps,mode="debug",data=data)
    else :
        if dwf :
            welcome()
        print(start_out)
        try :
            main(dps,mode="",data=data)
        except :
            pass

if __name__ == "__main__":
    if len(sys.argv) > 1 :
        start("main",debug=sys.argv[1])
    else :
        start("main",debug=None)
