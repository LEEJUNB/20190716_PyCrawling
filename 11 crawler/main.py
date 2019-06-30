import requests
from bs4 import BeautifulSoup as bs # bs4 패키지의 BeautifulSoup모듈

# URL의 내용을 가져오기에 get을 사용
URL = "https://academy.nomadcoders.co/p/instaclone-2-0"
rq = requests.get(URL)

soup = bs(rq.content,'html.parser') # 첫인자 : 가져온URL의 컨텐츠, 두번째인자 : html parser 작성
print(soup)