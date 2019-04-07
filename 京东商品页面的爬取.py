import requests
url = "https://item.jd.com/41502835402.html"
try:
    r = requests.get(url)
    r.raise_for_status()  # 如果状态不是200，引发HTMLText异常
    r.encoding = r.apparent_encoding
    print(r.text[:1000])
except :
    print("爬取失败")
