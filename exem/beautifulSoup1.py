from bs4 import BeautifulSoup as bs
import requests as req

url = "https://www.naver.com/"
res = req.get(url)
soup = bs(res.text , 'html.parser')
print(soup.title)