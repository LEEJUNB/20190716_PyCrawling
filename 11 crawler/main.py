import requests
from bs4 import BeautifulSoup as bs

URL = "https://academy.nomadcoders.co/p/instaclone-2-0"

# http 상태코드를 통해 정상적으로 처리가 됐다면 작동하도록 만들자
def get_tags() : 
    tags_list = [] # 결과값을 리스트객체로 만들자
    rq = requests.get(URL)
    print(rq.status_code) # http상태코드 출력
    if rq.status_code == 200 : # 정상처리됐다면
        soup = bs(rq.content,'html.parser') 
        
        # 리스트형태, 객체형태로 반환되기에 li_list에 할당함
        li_list = soup.find_all('div',class_= 'col-sm-12 course-section') 
        for li in li_list :
            ul = li.select('div > ul') # li도 BeautifulSoup의 메소드사용가능
            # ul객체도 li하나하나를 가지는 리스트객체 이므로 for문 사용
            for l in ul : 
                tags_list.append(l.get_text()) # 결과값을 리스트객체로 만듦
        return tags_list
    else : 
        raise Exception('응답 코드가 다릅니다')
                
        

 