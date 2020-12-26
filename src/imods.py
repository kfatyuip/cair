import re
import threading
import time

def funcplay(strs) :
    import fun
    return fun.funplay(strs)

def space(scan) :
    space = 0
    for i in scan :
        if i == " " :
            space += 1
    if space == len(scan) :
        return True
    else :
        return False

def main(scansc) :
    while True :
        scan = input(scansc)
        if scan == "cair" :
            main()
        elif scan == "exit" :
            ids.cair_exit()
            sys.exit(0)
        elif scan.split(" ")[0] == "run" and len(scan.split(" ")) > 1 :
            os.system(scan.split(" ")[1])
        elif space(scan) == True :
            continue
        elif scan == "更新" or scan == "检查更新" :
            from mod import check
            check.check(version,mi=data.get("MI"))
            continue
        elif scan == "cair日报" or scan == "日报" or scan == "头条" or scan == "新闻" :
            from mod import news
            news.connect(mode)
            continue
        elif re.match("下载:",scan) :
            url = re.sub("下载:","",scan)
            from mod import cwfd
            cwfd.download(url=url,file_path=os.path.basename(url))
            continue
        elif re.match("转巴祖木语:",scan) :
            cen = re.sub("转巴祖木语:","",scan)
            from mod.bzm import zbzm
            print(zbzm.translate(cen))
            continue
        elif re.match("巴祖木语转:",scan) :
            cen = re.sub("巴祖木语转:","",scan)
            from mod.bzm import bzmz
            print(bzmz.translate(cen))
            continue
        elif scan == "start server" or scan == "server" or scan == "start crsr" or scan == "crsr" :
            from mod.crsr import server
            server.main()
        elif re.match("转叽叽喳喳语:",scan) :
            cen = re.sub("转叽叽喳喳语:","",scan)
            from mod.jjzz import zjjzz
            print(zjjzz.translate(cen))
            continue
        elif re.match("叽叽喳喳语转:",scan) :
            cen = re.sub("叽叽喳喳语转:","",scan)
            from mod.jjzz import jjzzz
            print(jjzzz.translate(cen))
            continue
        elif re.match("天气预报:",scan) :
            city = re.sub("天气预报:","",scan)
            from mod import weather
            weather.main(city)
            continue
        elif scan == "bash" or scan == "sh" or scan == "zsh":
            if thisos != "Windows" :
                print("CAIR SHELL....")
                os.system(scan)
                continue
            else :
                ids.output("在?什么时候换的Windows?")
        elif scan == "cmd" or scan == "command" :
            if thisos == "Windows" :
                print("CAIR CMD....")
                os.system(scan)
                continue
            else :
                ids.output("在?什么时候换的Linux/macOS?")
        elif scan == "cls" and thisos == "Windows" :
            os.system(scan)
        elif scan == "clear" and thisos != "Windows" :
            os.system(scan)
        elif scan == "清屏" :
            os.system("cls" if thisos == "Windows" else "clear")
        elif funcplay(scan) :
            continue
        elif scan == "" :
            continue
        elif re.match("ip",scan) :
            from mod.fun.ip import getip
            print(getip())
            continue
        elif re.match("转base64:",scan) :
            from base64 import b64encode
            scan = re.sub("转base64:","",scan)
            print(str(b64encode(scan.encode())).replace("b","").replace('\'',""))
            continue
        elif re.match("base64转:",scan) :
            from base64 import b64decode
            scan = re.sub("base64转","",s)
            print(str(b64decode(scan).decode()))
            continue
        else :
            from fun import ask
            scan = ask(scan)
            if scan != "err" :
                print(scan)
            else :
                print("日常听不懂:(")
