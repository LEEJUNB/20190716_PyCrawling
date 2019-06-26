def sum(x, y, default=1) : 
    return x + y + default

#default값을 주지 않을시
#default값은 초기값('1')으로 대체
x = 1
y = 1
print(sum(x,y)) # 3
print(sum(x,y,10))  # 12

def sum_2(x, *y) : 
    sum_list = []
    for i in y : 
        sum_list.append(i)
    print(sum_list)

sum_2(1,1,2,3,4,5) # [1,2,3,4,5] 출력

def sum_3(x, *y) :
    result = 0
    for i in y :
        result += i
    print(result)

sum_3(1,1,2,3,4,5) # 15

