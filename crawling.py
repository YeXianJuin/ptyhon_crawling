import requests
from bs4 import BeautifulSoup

#圖書館抓取關鍵字"黑豹"資料

x=requests.get("https://opac.lib.ncu.edu.tw/search*cht/a?searchtype=Y&searcharg=%E9%BB%91%E8%B1%B9&SORT=D&submit=%E6%9F%A5%E8%A9%A2")
soup = BeautifulSoup(x.text, "html.parser")
span=soup.select(".briefcitTitle")
r=[]
for link in span:
	result=link.select("a")
	r.append(result[0].text)
for prin in r:
	print(prin.split("/")[0])

