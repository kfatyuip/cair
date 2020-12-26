def decode(s):
    return ''.join([chr(i) for i in [int(b, 2) for b in s.split(' ')]])

def translate(s) :
    s = s.replace("叽","0")
    s = s.replace("喳","1")
    result = decode(s)
    return result

if __name__ == "__main__" :
    while True :
        print(translate(input("请输入要翻译的叽叽喳喳语:")))
