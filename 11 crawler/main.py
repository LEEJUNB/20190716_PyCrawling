#인터프리터, 객체지향
# pip
# 객체란? 속성과 메서드로 구성
# 대상을 추상화 한다는 의미
# 추상화한다? 핵심적 개념과 특징의 집합
# 고양이 : 객체
# 점프, 행동 : 메서드
# 색상, 몸무게 : 속성

# 클래스? 객체를 추상화(개념,특징 집합)하여 담는 틀
# 즉, 클래스란 메서드, 변수, 속성선언
# 클래스 선언방법. class 클래스명() : __init__(self) : 생성자

class man() : 
    def __init__(self) :
        print("생성자")

yoman = man()

# 클래스에는 다음과 같이 2가지의 변수(속성)이 존재
# 클래스변수(공유), 인스턴스변수(개별)

class manpower() : 
    race = "Asian" # 공유되는 값인 클래스 변수

    def __init__(self,pos) : # self가 붙은 변수인 인스턴스 변수
        self.position = pos # pos인자에 값 할당하기

JBLEE = manpower("Chief Executive Officer") # 클래스를 통해 pos값 할당
print(JBLEE.race) # 클래스변수출력
print(JBLEE.position) # 인스턴스변수출력


class domain() : 
    territory = "Asia" # class variable
    
    def __init__(self,nation) : # instance variable
        self.Asia_nation = nation

OceanHoldings = domain("singapore")
NationHoldings = domain("Vietnam")
print(OceanHoldings.territory)
print(OceanHoldings.Asia_nation)
print(NationHoldings.Asia_nation)

# 인스턴스 변수 self가 붙은 변수
# 객체에 속한 함수(메서드)를 선언하자. 객체에 속해있지 않다면 그냥 함수
# def 메서드명(self,인자....) : 
# self 키워드는 인스턴스 메서드의 첫번째인자로 있어야만한다.

