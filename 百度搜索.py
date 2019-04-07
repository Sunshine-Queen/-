import requests
keyword="python"

try:
    kv={'wd':keyword}
    r = requests.get("http://www.baidu.com/s",params=kv)
    print(r.request.url)
    r.raise_for_status()  # 如果状态不是200，引发HTMLText异常
    print(len(r.text))
except :
    print("爬取失败")