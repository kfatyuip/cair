def encode(s):
    return ' '.join([bin(ord(c)).replace('0b', '') for c in s])

def translate(s) :
    s = encode(s)
    s = s.replace("0","叽")
    s = s.replace("1","喳")
    return s

if __name__ == "__main__" :
    while True :
        print(translate(input("请输入一个句子:")))
