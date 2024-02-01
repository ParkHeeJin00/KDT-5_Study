#---------------------------------------------
# List 자료형의 연산 살펴보기
# - 산술연산
# - 비교연산
# - 맴버연산자
#---------------------------------------------
# 1~50 범위의 2의 배수로 구성된 리스트 생성
twoNums = list(range(2,51,2))

# 산술연산 => 덧셈(+), 곱셈(*)-------------------
print( twoNums + ["A","B"])

datas = twoNums + ["A","B"]
print(datas)

# list + str => list + list(str)
print( twoNums + list("ABC"))

# list + str => str(list) + str
print( str(twoNums) + "ABC")
aa = str(twoNums)
print(aa[0])

# list * int => int만큼 원소를 반복해서 하나의 list
print(twoNums * 3)

# 멤버 연산 => in / not in ------------------------
#         => 결과 : True/Fasle
print("C" in datas)
print(1 in datas)
print(2 in datas)
