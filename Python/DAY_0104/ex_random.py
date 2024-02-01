# ----------------------------------------------
# 모듈(Module) : 특정 목적의 변수, 함수, 클래스를 하나의 파일에 담은 것
# - 예: 수학 관련 변수, 함수, 클래스 => math.py
#       파이썬 기본 제공 변수, 함수, 클래스 => builtin.py
# - 사용법 : import 모듈명
# - 모듈의 기능 사용법 : 모듈명.변수명
#                     모듈명.함수명()
# ----------------------------------------------
import random   # 임의의 수를 추출해주는 변수, 함수, 클래스가 있는 모듈
import math     # 수학 관련 변수, 함수, 클래스가 있는 모듈

# 모듈 안에 있는 변수, 함수, 클래스 사용
print(math.pi)

print(math.factorial(5))
# c -  클래스(앞 자리가 대문자) / v - 함수
print(random.random())   ## [0,1) : 0은 포함이 되고 1은 포함이 안됨

# 0.0 <= ~ <= 1.0 사이의 임의의 실수 추출 => random() 함수
for i in range(10):
    print(random.random())

# 1 <= ~ <= 10 정수를 추출
for i in range(10):
    print(int(random.random() * 10)+1)

# a <= ~ <= b 사이의 임의의 정수 추출 => randint() 함수
for i in range(10):
    print(random.randint(1,10), end = " ")
print()

# 로또 프로그램

myLotto = set()

End_point = 6    # 변수를 지정하고 나중에 이 변수값만 바꾸는게 편리

while True:
    if len(myLotto) == End_point: break
    myLotto.add(random.randint(1,45))

print(f'myLotto => {myLotto}')