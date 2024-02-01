# ----------------------------------------------
# 컨프리헨션 (Comprehension)
# - List Comprehension, Dict Comprehension, Set Comprehension
# ----------------------------------------------
# [실습1]  aList의 원소 값을 제곱한 값을 원소로 가지는 bList를 생성하세요
aList = [1,2,3,4]

bList = []
for a in aList:
    bList.append(a**2)

print(f'aList => {aList}')
print(f'bList => {bList}')

cList = [a**2 for a in aList]
print(f'cList => {cList}')

# [실습2] aList의 원소 값 중에서 짝수인 데이터만 제곱한 값을 원소로 가지는 bList 생성하세요
bList2 = []
for a in aList:
    if not a%2:   # not False => True     ## if a%2:
        bList2.append(a**2)

print(f'bList2 => {bList2}')

# 컨프리헨션 방식
cList2 = [a**2 for a in aList if not a%2]  # a%2 = 0 => if not 0 => True => for문 시행
#        ----  ------------- ----------
#        (3)       (1)           (2)
# (2)에서 True인 경우만 (3) 실행
print(f'cList2 => {cList2}')

# [실습3]  aList의 원소 값중에서 짝수인 데이터는 제곱, 홀수인 데이터는 그대로
# 저장한 bList를 생성하세요
# 일반적 for 방식
bList3 = []
for a in aList:
    if not a%2:   # not False => True     ## if a%2:
        bList2.append(a**2)
    else:
        bList3.append(a)
print(f'bList3 => {bList3}')

# list 컨프리헨션 방식
cList3 = [a**2 if not a%2 else a for a in aList ]
#        ---- ---------- ------ ---------------
#        (3-T)    (2)    (3-F)       (1)
print(f'cList3 => {cList3}')


# dict 컨프리헨션 방식
# cList3 = { a:a**2 if not a%2 else a for a in aList }
#         ---- ---------- ------ ---------------
#         (3-T)    (2)    (3-F)       (1)
