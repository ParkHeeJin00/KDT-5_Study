# ----------------------------------------------------------
# 함수와 클래스
# ----------------------------------------------------------
# 변수에 어떤 데이터를 저장하고 있는 지 확인 함수 => type(변수명)
data = 1 ## 변수는 주소값을 저장하는 값 -> 참조변수
print(f'data Type : {type(data)}')   ## Type을 알기 위해선 주소값이 저장되어있는 스택영역에 가서 그 주소값이 지정하는 힙영역에 가서 타입을 파악해야함

data = ''
print(f'data Type : {type(data)}')

# 함수명의 타입
print(f'id() Type : {type(id)}')  ## class type

# 사용자 정의 함수 생성 --------------------------------------------
# 함수 기능 : 2개 정수 더한 후 결과 출려 기능
# 함수 이름 : addTwo
# 매개 변수 : n1,n2
# 함수 결과 : 없음
# -------------------------------------------------------------
def addTwo(n1,n2):
    print(n1+n2)

# 함수의 타입 출력 ====> type() 내장함수 사용
print(type(addTwo))   # 소괄호 빼고 함수명만 넣으면 됨  => class function type => 함수는 class 객체임

# ------------------------------------------------------------------
# 함수와 변수
# - 함수명은 코드의 시작주소를 저장하고 있음
# - 함수명을 변수에 대입 가능
# ------------------------------------------------------------------
test = addTwo   # addTwo 함수의 주소값을 참조 => 해당 변수를 함수와 같이 사용할 수 있음
## =! test = addTwo() => 함수를 호출한 결과를 넣는 것

print(f'test => {id(test)}, {type(test)}')
print(f'addTwo => {id(addTwo)}, {type(addTwo)}')

test(1,2)  ## 함수처럼 동작함
addTwo(1,2)

# ------------------------------------------------------------------
# [활용 예]
# - 1~10 범위에서 임의의 정수 5개를 저장
# - 중복된 정수 저장 가능
# ------------------------------------------------------------------
import random

data = []
for i in range(5):
    data.append(random.randint(1,10))
print(data)

# 5개의 정수에서 최댓값, 최솟값, 합계, 내림차순 정렬된 값 출력하기

print(f'최대값 : {max(data)}\n최솟값 : {min(data)}\n내림차순 정렬된 값 : {sorted(data, reverse=True)}\n합계 : {sum(data)}\n갯수 : {len(data)}')

# 여너래긔 함수 이름을 변수에 저장 => 리스트 사용함
funs = [max, min, sorted, sum, len]
for f in funs:
    if f==sorted:     ## 매개변수가 있거나 해당 함수의 조건이 따로 있을때 조건문 사용
        print(f(data, reverse=True))  # reverse는 디폴트 매개변수 -> 매개변수 값을 바꾸기 위해 조건문 적용
    else:
        print(f(data))

## 위와 똑같이 출력하기 위해서는 dict에 담으면 됨
funsDict = {'최대값':max,'최소값':min,'내림차순 정렬된 값':sorted,'합계':sum,'갯수':len}
for m, f in funsDict.items():
    if f == sorted:
        print(f'{m} :' , f(data, reverse=True))   # f가 리스트 내에 존재하는 함수이기 때문에 f(data)로 입력
    else:
        print(f'{m} :', f(data))