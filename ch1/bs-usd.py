from bs4 import BeautifulSoup
import urllib.request as req

url = "http://finance.naver.com/marketindex/"
res = req.urlopen(url)

soup = BeautifulSoup(res, "html.parser")

price = soup.select("div.head_info > span.value").string
print("usd/krw =", price)