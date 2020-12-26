import sys

def str_to_hex(s):
    return ' '.join([hex(ord(c)).replace('0x', '') for c in s])

def translate(s) :
    fy = str_to_hex(s)
    result = ""
    for i in range(len(fy)) :
        if fy[i] == "0" :
            result += "α"
        if fy[i] == "1" :
            result += "ω"
        if fy[i] == "2" :
            result += "#"
        if fy[i] == "3" :
            result += "%"
        if fy[i] == "4" :
            result += "$"
        if fy[i] == "5" :
            result += "!"
        if fy[i] == "6" :
            result += "?"
        if fy[i] == "7" :
            result += ":"
        if fy[i] == "8" :
            result += "@"
        if fy[i] == "9" :
            result += "+"
        if fy[i] == "a" :
            result += "="
        if fy[i] == "b" :
            result += "&"
        if fy[i] == "c" :
            result += "¥"
        if fy[i] == "d" :
            result += "§"
        if fy[i] == "e" :
            result += "№"
        if fy[i] == "f" :
            result += "㏑"
        if fy[i] == " " :
            result += ";"
    return result

if __name__ == "__main__" :
    if len(sys.argv) == 2 :
        with open(sys.argv[1],mode="r") as f:
            print(translate(f.read()))
    else :
        while True :
            try :
                inp = input("请输入要翻译的句子:")
                print(translate(inp))
            except :
                print("NULL")
