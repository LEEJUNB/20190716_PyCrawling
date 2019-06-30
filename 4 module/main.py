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

