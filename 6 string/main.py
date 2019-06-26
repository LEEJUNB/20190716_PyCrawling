# 스트링형
test1 = "Life is too short, %s %s %s"
#result1 = test1 % "You need python."
result1 = test1 % ("You","need","python.")
print(result1)

# 정수형
test2 = "Life is too short %d"
result2 = test2 % 10
print(result2) # Life is too short 10

test3 = "Life is too short, %.2f"
result3 = test3 % 100
print(result3) # Life is too short, 100.00

# 포맷함수는 {}를 쓰고 타입은 삽입한 내용에 따라 바뀐다.
test4 = "Life is too short, {} {} {}"
result4 = test4.format("You","need", 10)
print(result4) # Life is too short, You need 10

test5 = "`You\" need \\Python my love"
print(test5) # `You" need \Python my love

test6 = "123\r89"
print(test6) # 893
