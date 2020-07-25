#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import sys
import os
import time
import requests
from bin.mod import agent

headers = agent.ua("chrome")
requests.packages.urllib3.disable_warnings()


def download(url, file_path,args=""):
    try :
        start = time.time()
        r = requests.get(url, stream=True, verify=False,headers=headers)
    except Exception :
        print("链接错误!请检查链接是否正确!")
        sys.exit(1)
    total_size = int(r.headers['Content-Length'])
    if total_size <= 1024 :
        c = 1
        e = "B"
    else :
        if total_size <= 1024 ** 2 :
            c = 1024
            e = "KB"
        else :
            if total_size <= 1024 ** 3 :
                c = 1024 ** 2
                e = "MB"
            else :
                if total_size <= 1024 ** 4 :
                    c = 1024 ** 3
                    e = "GB"
                else :
                    if total_size <= 1024 ** 5 :
                        c = 1024 ** 4
                        e = "TB"
    print("文件大小:",round(int(r.headers['Content-Length']) / int(c),2),e)
    temp_size = 0

    if args == "-o" :
        save = sys.argv[3]
    else :
        save = file_path

    fj = 0

    with open(save,mode="wb") as f:
        for chunk in r.iter_content(chunk_size=1024):
            fj += 1
            sl = int(r.headers['Content-Length']) % fj
            if chunk:
                temp_size += len(chunk)
                f.write(chunk)
                f.flush()
                done = int(50 * temp_size / total_size)
                sys.stdout.write("\r[%s%s] %d%%" % ('█' * done, ' ' * (50 - done), 100 * temp_size / total_size))
                sys.stdout.flush()
    print()
    end = time.time()
    spte = end - start
    spter = round(spte,2)
    if int(spter) <  60 :
        sp = spter
        spdw = "秒"
        if int(spter) >= 60:
            sp = spter / 60
            spdw = "分"
            if int(spter) >= 60 ** 2 :
                sp = spter / 60 ** 2
                spdw = "时"
    else :
        sp = "???"
        spdw = "???"
    print("用时:",sp,spdw)


if __name__ == '__main__':
    if len(sys.argv) >= 2 :
        if sys.argv[1] != "--help" :
            print("CWFD下载器")
            print("Copyright: ©CRDT Stduio")
    try :
        if len(sys.argv) != 1 :
            if sys.argv[1] != "--help" and sys.argv[1] != "--help":
                url = sys.argv[1]
            else :
                if sys.argv[1] == "--help" :
                    print("cwfd + url + (args)")
                    print("可以在终端中在后面写链接")
                    print("链接后面加-o参数就可以下载命名后的文件")
                    sys.exit()
        else :
            print("请输入cwfd --help以获得帮助")
            sys.exit()
        if url.find("https://") == -1 :
            if url.find("http://") == -1 :
                    url = "http://" + url
        path = os.path.basename(url)
        if len(sys.argv) == 4 :
            if sys.argv[2] == "-o" :
                download(url,path)
        else :
            download(url, path)
    except Exception :
        print("程序错误!请检查程序代码是否有错误!")
        time.sleep(1)
        sys.exit()
