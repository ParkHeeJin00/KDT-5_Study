# ------------------------------------------------------
# 참조형 변수 => 데이터의 주소 저장
# ------------------------------------------------------

# 저장된 데이터 & 변수 타입 관계 ----------------------------

num = 12
print(f'num => {id(num)}, {type(num)}')

num = 3.
print(f'num => {id(num)}, {type(num)}')

num = 'Good'
print(f'num => {id(num)}, {type(num)}')

num1 = []
print(f'num1 => {id(num1)}, {type(num1)}')

num2 = [11,22.1]
print(f'num2 => {id(num2)}, {type(num2)}')
print(f'num2[0] => {id(num2[0])}, {type(num2[0])}')
print(f'num2[1] => {id(num2[1])}, {type(num2[1])}')

print("=================================================")
num = 'Happy'
print(f'num => {id(num)}, {type(num)}')

num2[0] = 100
print(f'num2 => {id(num2)}, {type(num2)}')   # list의 주소값은 변함없음
print(f'num2[0] => {id(num2[0])}, {type(num2[0])}')     # list 내의 원소의 주소값은 변함

num2 = num1   # 이렇게 해야 list의 주소값이 변함
print(f'num2 => {id(num2)}, {type(num2)}')
print(f'num1 => {id(num1)}, {type(num1)}')
