test = [1,2,3]

try : 
    print(test[3])
except : 
    print("index Error")
finally : 
    print("must start")

# 실행결과
# index Error
# must start

test_num = 10
if test_num == 10 :
    raise Exception("test is 10.")

"""
Traceback (most recent call last):
  File "main.py", line 16, in <module>
    raise Exception("test is 10.")
Exception: test is 10.
"""