from bin import init

if init.__it__ == "Standard" :
    name = "CAIR"
else :
    name = init.__it__

def output(s) :
    print("%s:|%s" % (name,s))
