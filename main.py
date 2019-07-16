import sub # 모듈명 sub
print(sub.sum(1,1)) #sub모듈의 sum함수 가져오기.특정 함수가져오려면 계속 입력해야.

# import sub 방식은 sub모듈에서 여러 함수, 속성가져와야하는 경우 번거로워
# 번거로움을 줄이기 위한 from키워드
from sub import sum
print(sum(1,1))

from sub import sum as s # sum이란 함수는 s로 부른다는 의미
print(s(1,1))

from package import pck as rename
print(rename.sum(1,2))

num_list = [0,2,3,4,5]

# 인덱스는 0부터 시작
print(num_list[0], num_list[-0], num_list[-1])

# 인덱스값 변경하기
num_list[0] = 1

# 반복문. 멤버쉽연산자인 in을 이용함
for i in num_list : 
    print(i)

# 슬라이싱 (범위) 시작 : 끝-1
print(num_list[0:3])
print(num_list[1:])

# 추가하기 append
num_list.append(6)
print(num_list)

# 마지막 리스트 삭제하기
del num_list[-1]
print(num_list)

# 길이 len이용하여 마지막 리스트 del하기
del num_list[len(num_list)-1]
print(num_list)

#dictonary
num_dict = {"key":"value","키":"값"}
print(num_dict["key"])

for k, v in num_dict.items():
    print(k,v)

# key값들만 반환
print(num_dict.keys())

# value값들만 반환
print(num_dict.values())

# 새 key,value 삽입
num_dict["append key"] = "append value"
print(num_dict)

# key의 value수정
num_dict["key"] = "new value"
print(num_dict)

# 삭제
del num_dict["key"]
print(num_dict)

# 없는 키의 값을 에러없이 찾는 방법
print(num_dict.get("nothing")) # None 출력