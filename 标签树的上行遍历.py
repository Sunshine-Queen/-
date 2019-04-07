import  requests
r = requests.get("http://python123.io/ws/demo.html")
demo=r.text
from  bs4 import BeautifulSoup
soup=BeautifulSoup(demo,"html.parser")
for parent in soup.a.parents:
    if parent is None:
        print(parent)
    else:
        print(parent.name)