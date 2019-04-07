import  requests

#通用代码框架，处理异常

def getHTMLText(url):
    try :
        r = requests.get(url,timeout=30)
        r.raise_for_status()#如果状态不是200，引发HTMLText异常
        r.encoding = r.apparent_encoding
        return  r.text
    except :
        return "产生异常"
    ##框架结束

if __name__=="__main__":
    url = "http://www.baidu.com"
    #url = ":www.baidu.com"
    print(getHTMLText(url))
