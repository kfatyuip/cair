#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
______________________________
__  ____/__    |___  _/__  __ \
_  /    __  /| |__  / __  /_/ /
/ /___  _  ___ |_/ /  _  _, _/
\____/  /_/  |_/___/  /_/ |_|

Developer : kfatyuip
Copyright : ©CRDT Studio 2020
Kernel : CAIR
Program Languge : Python
CAIR is a command-line-oriented robot
The full name of the CAIR is CRDT Artificial Intelligence Robot 
CRDT Studio All rights reserved
"""


import sys
import platform
from bin import init
from bin import main

init.path(sys.argv[0])
__version__ = init.__version__
this_os = platform.system()
dps = init.dps

dwf = True
status = init.cair_start()
if status.get("welcome") == True :
    dwf = False
MI = status.get("MI")
data = status

def output(strs) :
    print("CAIR:|" + str(strs))

def welcome() :
    print("欢迎使用CAIR人工智能机器人")
    print("操作系统: %s" % platform.platform())
    print("版本: %s" % init.__version__,"类型: %s版" % init.__vt__,"发行版本: %s" % init.__it__)
    print("版权所有: CRDT Studio","开发者: %s" % init.__author__)
    
start_out = "-" * 30

def start(mode="main",debug=None) :
    if debug != None :
        if debug == "debug" :
            if dwf :
                welcome()
            output("##开发者DEBUG模式已启动##")
            print(start_out)
            main.main(dps,mode="debug",data=data)
    else :
        if dwf :
            welcome()
        print(start_out)
        try :
            main.main(dps,mode="",data=data)
        except :
            pass

if __name__ == "__main__":
    if len(sys.argv) > 1 :
        start("main",debug=sys.argv[1])
    else :
        start("main",debug=None)
