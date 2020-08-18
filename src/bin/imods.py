import re
import threading
import time

ok = True

class myThread(threading.Thread):
    def __init__(self,name,s):
        threading.Thread.__init__(self)
        self.name = name
        self.s = s
    def run(self):
        if self.name == "a" :
            self.ar = func_A(self.s)
    def get_result(self) :
        return self.ar

def main(s) :
    a = myThread("a",s)
    a.start()
    a.join()
    if a.get_result() :
        return True
    else :
        return False

def func_A(s) :
    if re.match("ip",s) :
        from bin.mod.fun.ip import getip
        print(getip())
        return ok
    elif re.match("转base64:",s) :
        from base64 import b64encode
        s = re.sub("转base64:","",s)
        print(str(b64encode(s.encode())).replace("b","").replace('\'',""))
        return ok
    elif re.match("base64转:",s) :
        from base64 import b64decode
        s = re.sub("base64转","",s)
        print(str(b64decode(s).decode()))
        return ok
    else :
        return False
