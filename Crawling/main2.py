import requests
from bs4 import BeautifulSoup as bs
from openpyxl import load_workbook as load


SAVE_DIR = "c:/Users/last2018/dev/python/basic/Crawling/Price.xlsx"

# body > div.contentWrapper > div.container > div.left_cont > div > div > div.news_head

def get_tags() : 
	tags_list = []
	rq = requests.get(URL)
	print(rq.status_code)
	if rq.status_code == 200 : 
		soup = bs(rq.content, 'html.parser')
		li_list = soup.find_all('div',class_="news_head")
		for li in li_list : 
			ul = li.select('h1')
			for l in ul : 
				tags_list.append(l.get_text())
		return tags_list
	else : 
		raise Exception('not 200')

def save_excel(get_tags) : 
	wb = load(SAVE_DIR)
	ws = wb.create_table('title')
	wb.save(SAVE_DIR)
	wb.close()