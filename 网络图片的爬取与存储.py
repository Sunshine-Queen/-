import requests
import os
# url="http://image.nationalgeographic.com.cn/2017/0211/20170211061910157.jpg"
url="https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=3587049538,3549681138&fm=26&gp=0.jpg"
root="D://pics//"
path=root+url.split('/')[-1]
try:
   if not os.path.exists(root):
       os.mkdir(root)
   if not os.path.exists(path):
        r=requests.get(url)
        with open(path,'wb')as f:
           f.write(r.content)
           f.close()
        print("文件保存成功")
   else :
            print("文件已经存在")
except:
    print("爬取失败")