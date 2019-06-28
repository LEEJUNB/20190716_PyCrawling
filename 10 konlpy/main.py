from konlpy.tag import Okt

ok = Okt() 

""" 
# 문자열에서 해시태그만을 추출
test = "안녕하세요. 오늘은 6월 입니다 #hash #man #Yoman"

for i in ok.pos(test,norm=True ) :
    if i[1] == 'Hashtag' : # 튜플의 첫번쨰 요소가 해시태그라면
        print(i)
"""
# 명사만을 추출해보자
# 리스트로 반환된다

test = "와썹 프로그래밍 요맨"
for i in ok.nouns(test) : # 고유명사를 기준으로 리스토로 반환해주는 nouns인자
    print(i)