import requests
url="https://www.amazon.com/adidas-Originals-Adilette-Shower-Sandal/dp/B0716XDK7N/ref=sr_1_3?ajr=3&pf_rd_p=20eab4f3-ac42-4579-923b-0d50e40834e4&pf_rd_r=NNDW40TJ97M54E5R0VR2&qid=1554113779&s=fashion-mens-intl-ship&sr=1-3"
try:
    kv = {'user-agent':'Mozilla/5.0'}
    r = requests.get(url,headers=kv)
    r.raise_for_status()  # 如果状态不是200，引发HTMLText异常
    r.encoding = r.apparent_encoding
    print(r.text[1000:2000])
except :
    print("爬取失败")