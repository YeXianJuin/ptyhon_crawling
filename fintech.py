import requests
from bs4 import BeautifulSoup

# 抓取fintech關鍵字相關文章
url="https://technews.tw/category/fintech/"
req=requests.get(url)

soup=BeautifulSoup(req.text,"html.parser")
title=soup.select(".entry-title")

r=[] #r是list (python中沒有陣列但有list)
for link in title:
	result=link.select("a")
	r.append(result[0].text)
#利用select將a抓出來，append(累加)在r上
for prin in r:
	print(prin+"\n")
