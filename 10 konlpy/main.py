from konlpy.tag import Okt

ok = Okt() # ok객체에 Okt패키지 할당
test = "Hello" # 문자열 객체

# ok.pos(test)은 리스트로 반환 
# pos메서드때문에 리스트 각각이 튜플로 반환
# 리스트이므로 반복문으로 하나씩 꺼낼수있음
for i in ok.pos(test) : 
    print(i)

