uas = {
    "ie" : "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; Zune 3.0)",
    "opera" : "Opera/9.80 (Windows NT 6.1; U; en-US) Presto/2.7.62 Version/11.01",
    "chrome" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
    "firefox" : "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:21.0) Gecko/20130331 Firefox/21.0",
    "safari" : "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4",
}

def ua(argv="random") :
    if argv == "ie" :
        return uas["ie"]
    elif argv == "opera" :
        return uas["opera"]
    elif argv == "chrome" :
        return uas["chrome"]
    elif argv == "firefox" :
        return uas["firefox"]
    elif argv == "safari" :
        return uas["safari"]
    else :
        import random
        return uas[("ie","opera","chrome","firefox","safari")[random.randint(0,3)]]
