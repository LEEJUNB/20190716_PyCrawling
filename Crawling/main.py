# from konlpy.tag import Okt # 한국어 말뭉치 처리

# ok = Okt()
# test = "Alread July"

# for i in ok.pos(test) :  #pos는 Okt패키지의 문자열을 튜플로 반환하는 메서드
#     print(i)
    
import requests
from bs4 import BeautifulSoup as bs

URL = "http://prod.danawa.com/info/?pcode=7162288&cate=11330083"
rq = requests.get(URL)

soup = bs(rq.content,'html.parser')
print(soup)

#productDescriptionArea > div > div.prod_spec > table > tbody

