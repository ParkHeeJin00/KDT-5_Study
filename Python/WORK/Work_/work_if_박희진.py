# [연습문제] 13.6

x = 5
if x != 10 :
    print("ok")

# [연습문제] 13.7

price = int(input())
cuponName = input()

if cuponName == "Cash3000":
    print(price - 3000)
elif cuponName == "Cash5000":
    print(price - 5000)
else:
    pass


# [연습문제] 14.6

written_test = 75
coding_test = True

if written_test>=80 and coding_test == True :
    print("합격")
else:
    print("불합격")

# [심사문제] 14.7
kor, eng, math, sic = map(int,input().split())

if 0<= kor <= 100 and 0<= eng <= 100 and 0<= math <= 100 and 0<= sic <= 100:
    if (kor + eng + math + sic)/4 >= 80:
        print("합격")
    else:
        print("불합격")
else:
    print("잘못된 점수")


# [연습문제] 15.3

x = int(input())

if 11<= x <=20:
    print("11~20")
elif 21 <= x <= 30:
    print("21~30")
else:
    print("아무것도 해당하지 않음")

# [심사문제] 15.4

age = int(input())
card = 9000

if 7<=age<=12:
    price = 650
    card -= price
elif 13<=age<=18:
    price = 1050
    card -= price
elif age<=19:
    price = 1250
    card -= price
else:
    pass
print(card)