# -----------------------------------------------
# 다양한 리스트 생성
# -----------------------------------------------
# 실수 데이터로 구성된 리스트 생성
floatNums = [4., 3.1, 6.3, 5.01]

# str 데이터로 구성된 리스트 생성
strNums = ['44', '56', '98']

# bool 데이터로 구성된 리스트 생성
boolNums = [False, False, True, True, True]

# 다양한 데이터 타입으로 구성된 리스트 생성
nums = ['100', 98, False, 7.12, 'Apple', True]


# 빈 리스트 생성
nums = []

# 리스트 안에 리스트 데이터로 구성된 리스트 생성
nums = [10, 20, 30, ['A', 'B'], 200, 100]

# 리스트의 요소 출력
print(f'num[0] => {nums[0]}, {type(nums[0])}')
print(f'num[1] => {nums[1]}, {type(nums[1])}')
print(f'num[2] => {nums[2]}, {type(nums[2])}')
print(f'num[3] => {nums[3]}, {type(nums[3])}')
print(f'num[4] => {nums[4]}, {type(nums[4])}')
print(f'num[5] => {nums[5]}, {type(nums[5])}')

print(f'num[3][1] => {nums[3][1]} {type(nums[3][1])}')
