# 1~10

print(1)
print(2)
print(3)
print(4)
print(5)
print(6)
print(7)
print(8)
print(9)
print(10)

# 1~10 => 데이터
nums = [1,2,3,4,5,6,7,8,9,10]   # list()함수 자동으로 소환

for n in nums:
    print(n, end =' ' if n != 5 else '\n')     # 5에서 줄바꿈하기
print("end")

if n>0:
    print(n)
    print(n)
    print(n)
    if n%2:
        print("홀수")
print("ok")
print("end")

# *찍기

for i in range(1,6):
    print("*"*i)



