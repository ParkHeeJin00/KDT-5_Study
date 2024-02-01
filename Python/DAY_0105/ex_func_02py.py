# ----------------------------------------------------
# 다양한 함수의 형태 - (1) 기본
# ----------------------------------------------------
# 함수 기능 : 팩토리얼은 계산 후 계산 결과를 반환해주는 기능
# 함수 이름 : factorial
# 매개 변수 : n
# 반 환 값 : 계산결과
# ----------------------------------------------------
def factorial(n):
    if not n:
        n = 1
    for i in range(1, n): n *= i
    return n

print(factorial(0))
# ----------------------------------------------------
# 함수 기능 : 팩토리얼은 계산 후 계산 결과를 반환해주는 기능
#           예시 결과 3! = 3 * 2 * 1
# 함수 이름 : factorial2
# 매개 변수 : n
# 반 환 값 : 계산결과
# ----------------------------------------------------
## 내가 짠 코드 - 개구림
def factorial2(n):
    print(f'{n}! : ',end ="")
    if not n :
        print(f'{n}! = 1')
    for i in range(n,0,-1):
        if i > 1:
            n *= i-1
        print(f'{i} *', end = " ") if i>1 else print (f'{i} =', end=" ")
    print(n)

print(factorial2(3))

# 강사님 코드
def factorial2(n) :
    strRet=f'{n}! = '
    intRet=1
    for n in range(n,0,-1) :
        strRet=strRet+str(n)
        strRet = strRet + (' * ' if n!= 1 else ' = ')
        intRet=intRet * n
    strRet = strRet + str(intRet)
    return strRet

print(factorial2(3))
