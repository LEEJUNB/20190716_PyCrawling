# from konlpy.tag import Okt # 한국어 말뭉치 처리

# ok = Okt()
# test = "Alread July"

# for i in ok.pos(test) :  #pos는 Okt패키지의 문자열을 튜플로 반환하는 메서드
#     print(i)
    
import requests
from bs4 import BeautifulSoup as bs
from openpyxl import load_workbook as load

URL = "http://prod.danawa.com/info/?pcode=7162288&cate=11330083"
SAVE_DIR = "c:/Users/last2018/dev/python/basic/Crawling/Price.xlsx"

def get_tags() : 
    tags_list = []
    rq = requests.get(URL)
    print(rq.status_code)
    if rq.status == 200 : 
        soup = bs(rq.content,'html.parser')
        li_list = soup.find_all('div',class_='prod_spec')
        for li in li_list : 
            ul = li.select('table > tbody > tr')
            for l in ul : 
                tags_list.append(l.get_text())
        return tags_list
    else : 
        raise Exception('not 200')

def save_excel(get_tags) : 
    wb = load(SAVE_DIR)
    ws = wb.create_sheet('rank')
    wb.save(SAVE_DIR)
    wb.close()