# [실습] ---------------------------------
# - 문자열 여러 개와 실수 여러 개를 입력 받기 => input() 1개만 사용
# - 첫번째 입력받은 값은 key
# - 두번째 입력받은 값은 value
# - 딕셔너리로 저장해 주세요.
# ---------------------------------------
data = input("문자열과 실수 여러 개 입력 \n단, 문자열과 실수 갯수 동일(예:aa bb cc, 1.1 2.2 3.3")

# 입력 형식이 맞을 경우만 딕셔너리에 저장
# - (1) 입력 "  ,   " 문자열 안에 ',' 존재 해야 함
# - (2) 문자열과 실수 갯수가 동일 해야 함
if ',' in data:
    #dataList = data.split(',')    #['aa bb cc', '1.1 2.2 3.3']
    #key = dataList[0].split()
    #value = dataList[1].split()
    key, value = data.split(',')
    key = key.split()
    value = value.split()
    if len(key) == len(value):
        dataDict = {}
        for num in range(len(key)):
            dataDict[key[num]] = float(value[num])
    #dataDict = dict(zip(key, value))
        print(f'dataDict : {dataDict}')
    else:
        print("정학한 형식이 아닙니다.")
else:
    print("정확한 형식이 아닙니다.")



# ---------------------------------------------------------
# 내장함수 zip()   ## 튜플로 묶어준다
# ---------------------------------------------------------
x = [1,2,3,4,5]
y = [11,22,33,44,55]
z = [111,222,333,444,555]

result = zip(x,y,z)
print(f'result => {type(result)}, {list(result)}')

