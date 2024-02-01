# ---------------------------------------------------
# 람다 표현식 또는 람다 함수
# - 람다 함수라고도 함!
# - 짧은 코드의 함수 또는 반복에서 재사용이 많지 않은 코드의 경우 표현
# - 문법 : lambda 매개변수1,..,매개변수n : 표현식
# - 결과 : 매개변수를 활용한 표현식 결과 값이 lambda 그 위치에 반환됨
# ---------------------------------------------------
def add(a,b):
    return a+b

def minus(a,b):
    return a-b

# 람다 함수 형태와 호출
print((lambda a,b:a+b)(4,5))
print((lambda a,b:a-b)(4,5))

# 람다 함수 변수에 저장
myAdd = lambda a,b:a+b
myMinus = lambda a,b:a-b

# 람다 함수 호출
print(myAdd)
print(myMinus)