# --------------------------------------------------------
# filter(함수명, 반복 가능 객체)
# - 조건에 맞는 데이터만 반환
#   -> 조건식에 True인 원소만 반환
# --------------------------------------------------------
# 예) 5초과 10 미만 데이터만 추출
a = [8,2,1,0,15,7,1,9,0,11]

def check(data):
    return data> 5 and data<10   # => return 값 : True or False

a = list(filter(check,a))
print(a)

# 람다 함수 사용
a = list((lambda data:data>5 and data<10,a))



# import random => random.py 파일에서 모든 변수, 함수, 클래스 가져오기
# from random import randint => rando.py 파일에서 randint 함수만 가져오기
# from random import randint, random => rando.py 파일에서 randint, random 함수만 가져오기

from functools import reduce

def f(x,y):
    return x+y

print(reduce(f,a))

# 람다 함수 사용    => 재사용하지 않는 함수를 정의하기 위해서 : 최대한 힙영역 쓰지 않기 위해
print(reduce(lambda x, y : x+y,a))