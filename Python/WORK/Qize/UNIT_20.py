# 20.7
for i in range(1,101):
    if i % 2 == 0 and i % 11 == 0:
        print("FizzBuzz")
    elif i % 2 == 0:
        print("Fizz")
    elif i % 11 == 0:
        print("Buzz")
    else:
        print(i)

# 20.8

start, stop = map(int,input().split())

if 1<=start<=1000 and 10<=stop<=1000 and start<stop:
    for i in range(start,stop+1):
        if i % 5 == 0 and i % 7 ==0:
            print("FizzBuzz")
        elif i % 5 == 0:
            print("Fizz")
        elif i % 7 == 0:
            print("Buzz")
        else:
            print(i)

# 코드 단축하기
if 1<=start<=1000 and 10<=stop<=1000 and start<stop:
    for i in range(start,stop+1):
        print('Fizz'* ( i % 5 == 0) +'Buzz' * (i % 7 == 0) or i)
