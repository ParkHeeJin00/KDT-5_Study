# ---------------------------------------------------
# pass => 그냥 지나감
# - 키워드는 아무 일도 하지 않고 아무 일도 일어나지 않음
# - 파이썬 문법 때문에 사용
#   if 조건문, for ~ in 반복문, while 반복문에서
#   실행 코드 부분이 없는 경우에 사용함!
# - 아직 문제 해결 방법 정해지지 않음을 나타냄!
# ---------------------------------------------------
num = 100
if num > 10:
    pass     # 향후 버전에서 기능 구현 예정
age = 30

for n in range(10):
    pass
print("그냥")

class A:
    pass