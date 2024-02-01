# [연습문제] 26.8

a = {i for i in range(1,101) if i % 3 == 0}
b = {i for i in range(1,101) if i % 5 == 0}

print(a & b)

# [심사문제] 26.9

aNum,bNum = map(int,input().split())
if aNum<0 or bNum<0:
    print('양의 정수를 입력하세요.')

a = set()
b = set()

for i in range(1,aNum+1):
    if aNum % i ==0 :
        a.add(i)

for i in range(1,bNum+1):
    if bNum % i == 0:
        b.add(i)

divisor= a & b
result=0
if type(divisor) == set :
    result = sum(divisor)
print(result)
