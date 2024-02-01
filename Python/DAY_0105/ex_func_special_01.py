# ----------------------------------------------------
# 다양한 함수의 형태 - 특별한 함수 (1)
# - 매개변수의 갯수를 유동적으로 가변으로 하는 함수
# - 형태 : def 함수명( *data ):     ## 튜플형
# - 가변 인자 함수
# - 매개변수 갯수 : 0개 ~ n개
# ----------------------------------------------------
# 2개 정수를 덧셈 후 결과를 반환하는 함수 생성 --------------
def addTwo(a,b):
    return a+b

# 5개 정수를 덧셈 후 결과를 반환하는 함수 생성 --------------
def addFive(a,b,c,d,e):
    return a+b+c+d+e

# 3개 정수를 덧셈 후 결과를 반환하는 함수 생성 --------------
def addThree(a,b,c):
    return a+b+c

# ----------------------------------------------------
# 함수 기능 : 전달 받은 숫자를 모두 덧셈한 결과 반환 기능
# 함수 이름 : addNumber
# 매개 변수 : *nums      # tuple 형식
# 반 환 값 : 계산결과
# ----------------------------------------------------
def addNumber( *nums ):
    ret = 0
    for i in nums:
        ret += i
    return ret

# 함수 사용 즉 함수 호출 ===================================
print(addNumber(1,2,3))
print(addNumber(10))
print(addNumber())

# *시퀀스/반복가능한 객체 => 내부에 모든 원소를 하나씩 풀어서 전달 : 언팩킹
print(addNumber(*range(1,11)))

a = [11,22,33,44,55]
aTuple = 'a','b','c'
aDict = {'jj':'Hong','age':100}

print(a)
print(*a, sep='-')
print(*aTuple, sep='-')
print(*aDict, sep='-')  ## 키값만 가지고 옴
print(**aDict,sep='-')  ## 키값과 밸류값 둘다 가지고 옴