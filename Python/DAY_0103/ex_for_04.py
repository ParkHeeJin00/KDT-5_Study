# -------------------------------------------------------
# 반복문과 내장함수 => map(), zip()  ## 반환값이 map, zip 타입임 -> 형변환 해야함
# -------------------------------------------------------
xList = ['1','3','5','7']

# xList 안에 모든 원소를 정수 int로 변환 후 저장해 부세요
xList[0] = int(xList[0])
xList[1] = int(xList[1])
xList[2] = int(xList[2])
xList[3] = int(xList[3])

for idx in range(len(xList)):    ## len(xList) - 0 ~ 3
    xList[idx] = int(xList[idx])
print(f'xList => {xList}')

# --------------------------------------------------------------------
# 시퀀스 또는 반복이 가능한 객체의 요소/원소에 적용 후 값을 다시 저장해야 하는 경우
# 자주 사용되는 기능으로 내장함수로 제공 => map()
# - 문법 : map(함수명, 시퀀스 또는 반복이 가능한 객체)   ## 함수명 적어야 함. 소괄호 적으면 안됨
# --------------------------------------------------------------------
# int 요소인 xList를 str 요소로 변환
result = list(map(str,xList))
print(f'result => {result}')

result = list(map(bool,xList))
print(f'result => {result}')


# --------------------------------------------------------------------
# list 데이터를 dict 데이터로 생성
# --------------------------------------------------------------------
x = ['std01','std02','std03']
y = [90,100,99]

# 방법 (1) --> 기호/부호 {}
xyDict = {}
xyDict['std01'] = 90
xyDict['std02'] = 100
xyDict['std03'] = 99

print(xyDict)

# 방법 (2) --> dict() 생성자 함수
xyDict2 = dict()
# xyDict['std01'] = 90
# xyDict['std02'] = 100
# xyDict['std03'] = 99
for idx in range(len(x)):
    xyDict2[x[idx]] = y[idx]

print(xyDict2)

# 방법 (3) --> dict( [ (키1,값1),(키2,값2), ...(키n,값n) ] ) 생성자 함수
xy = []
for idx in range(len(x)):
    xy.append((x[idx], y[idx]))
xyDict3 = dict(xy)

print(xyDict3)

# 방법 (4) --> dict( [ (키1,값1),(키2,값2), ...(키n,값n) ] ) 생성자 함수
# By 내장함수 zip()
xyDict4 = dict(zip(x,y))

print(xyDict4)