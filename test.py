class Cat() :
    species = "russian blue" # class 변수로 선언. 공통적으로 사용되기에

     #개별적으로 사용되는 instance변수. 객체에서 사용됨
     #각 객체가 개별적으로 가지는 메서드에서 사용되는 키워드
     #클래스변수와 선언하는 위치가 다르고 선언 키워드가 달라
    def __init__(self, name) :
        self.name = name 
    

# 선언한 Cat객체 사용하기.이렇게 선언하면 Cat객체의 __init__메서드가 자동 생성됨(생성자)
cat1 = Cat("na") # 생성자에 인자로 넘겨준 "na"
cat2 = Cat("nana") 

print(cat1.species) # russian blue 출력
print(cat2.species) # russian blue 출력

print(cat1.name) # na 출력
print(cat2.name) # nana 출력
