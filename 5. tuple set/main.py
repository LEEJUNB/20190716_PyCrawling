num_tuple = (1,2,3)
print(num_tuple)

num_set = {1,2,3,4,5,6,6}
print(num_set)

#추가하기
num_set.add(4)
print(num_set)

#set은 집합이므로 set끼리 연산가능
set1 = {1,2,3,4}
set2 = {1,2,3,5,6}
#교집합
print(set1 & set2)
#합집합
print(set1 | set2)
#차집합
print(set1 - set2)

# 컬렉션연산은 연산으로 리스트값 수정가능
test_list= [1,2,3]
sub_list = [1,2,3]
print(test_list + sub_list)
print(test_list * 3)

# 컬렉션의 특징을 살려보자
# list(), dict(), set(), tuple() 생성자
test_li = [1,2,3,1,2,3]
print(set(test_li)) # set 을 사용하여 중복값제거
print(list(test_li)[0]) # 1 출력
print(tuple(test_li))