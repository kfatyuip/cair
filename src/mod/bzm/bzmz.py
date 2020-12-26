import sys

def hex_to_str(s):
    return ''.join([chr(i) for i in [int(b, 16) for b in s.split(' ')]])

def translate(fy) :
    result = ""
    for i in range(len(fy)) :
        if fy[i] == "α" :
            result += "0"
        if fy[i] == "ω" :
            result += "1"
        if fy[i] == "#" :
            result += "2"
        if fy[i] == "%" :
            result += "3"
        if fy[i] == "$" :
            result += "4"
        if fy[i] == "!" :
            result += "5"
        if fy[i] == "?" :
            result += "6"
        if fy[i] == ":" :
            result += "7"
        if fy[i] == "@" :
            result += "8"
        if fy[i] == "+" :
            result += "9"
        if fy[i] == "=" :
            result += "a"
        if fy[i] == "&" :
            result += "b"
        if fy[i] == "¥" :
            result += "c"
        if fy[i] == "§" :
            result += "d"
        if fy[i] == "№" :
            result += "e"
        if fy[i] == "㏑" :
            result += "f"
        if fy[i] == ";" :
            result += " "
    return hex_to_str(result)

if __name__ == "__main__" :
    if len(sys.argv) == 2 :
        with open(sys.argv[1],mode="r") as f :
            print(translate(f.read()))
    while True :
        try :
            inp = input("请输入要翻译的句子:")
            print(translate(inp))
        except :
            print("NULL")