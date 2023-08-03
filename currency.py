import requests as req
import re

url = "https://finance.naver.com/marketindex/"

res = req.get(url)
body = res.text

#r = re.compile(r"미국 USD.*?value\">(.*?)</",re.DOTALL)
r = re.compile(r"h_lst.*?blind\">(.*?)</span>.*?value\">(.*?)</",re.DOTALL)
captures = r.findall(body)

print("------------")
print("환율 계산기")
print("------------")
print("")

for c in captures:
    print(c[0] + " : " + c[1])

print()
usd = float(captures[0][1].replace(",",""))
won = input("달러로 바꾸길 원하는 금액(원)을 입력해주세요 : ")
won = int(won)
dollar = won / usd
dollar = int(dollar)
print(f"{dollar} 달러 환전되었습니다.")