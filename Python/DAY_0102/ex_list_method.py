
#----------------------------------------------------------------------
# 메서드 => 특정 데이터 타입의 전용 함수를 메서드(Method)라고 부름
# - 범용의 함수와 식별하기 위해서 지정한 호칭
# - 사용법 : 데이터.메서드명 또는 변수명.메서드명
#----------------------------------------------------------------------
# List 전용 메서드 살펴보기 ===============================================
# [1] 리스트에 데이터 추가해주는 메서드 => append() 맨 끝에 원소로 추가
nums = []

print(f'nums : {len(nums)}개')

nums.append(10)
nums.append('one')
nums.append(True)
print(f'nums : {len(nums)}개')

# [1] 리스트에 데이터 추가해주는 메서드 => insert(위치 인덱스, 데이터) 지정 위치에 추가
nums.insert(0,2024)
print(f'nums : {len(nums)}개, {nums}')

nums.insert(-1,["ABC", "DEF"])
print(f'nums : {len(nums)}개, {nums}')

# 'DEF' 데이터 삭제해주세요
del nums[-2][1]
print(f'nums : {len(nums)}개, {nums}')


# 리스트 안에 모든 원소 삭제해서 빈 리스트 만들어주세요
del nums[:]
print(f'nums : {len(nums)}개, {nums}')

# [2] 리스트 안에 원소/요소 정렬해주는 메서드 => sort() 오름차순 정렬
# - 오름차순 : 작은 데이터 >>> 큰 데이터
nums.append(98)
nums.append(-1)
nums.append(2)
nums.append(0.1)
nums.append(6)

nums.sort() # sort의 반환값은 none. 변수명에 저장하면 none이 됨. 원본 자체가 바뀌는 메서드. 저장하지 말 것
print(f'nums : {len(nums)}개, {nums}')

# 내림차순 : 큰 데이터 >>> 작은 데이터 순서로
nums.sort(reverse=True) # 역순 매개변수 값을 True로 설정
print(f'nums : {len(nums)}개, {nums}')

# [3] 리스트 안에 원소/요소의 현재 위치를 반대로 뒤집어 주는 메서드 => reverse()
# 원소/요소 데이터 값 비교 안함! 순서만 변경함!
nums.reverse()
print(f'nums : {len(nums)}개, {nums}')

# [4] 리스트 안에 원소/요소를 삭제해주는 메서드 => remove()
# - 리스트에서 지정된 값의 원소 삭제
# - 없는 값/데이터 삭제 요청 시 Error 발생시킴!!
nums.remove(6)
print(f'nums : {len(nums)}개, {nums}')

# [5] 리스트 안에 모든 원소/요소를 삭제해주는 메서드 => clear{}
nums.clear()
print(f'nums : {len(nums)}개, {nums}')

# [6] 리스트에 원소/요소를 꺼내는 메서드 => pop()
nums.append(98)
nums.append(-1)
nums.append(2)
print(f'nums : {len(nums)}개, {nums}')

# 제일 마지막 원소/요소 데이터 꺼내기 => pop()
nums.pop()
print(f'nums : {len(nums)}개, {nums}')

# 특정 위치의 원소/요소 데이터 꺼내기 => pop(인덱스)
nums.pop(0) # 반환값 있음
print(f'nums : {len(nums)}개, {nums}')

# [7] 리스트에서 특정 원소/요소 데이터가 몇개 존재하는지 카운팅해주는 메서드 => count(특정 데이터)
print(nums.count('A'))
print(nums.count(-1))

# [8] 리스트를 확장시켜주는 메서드 => extend(여러개의 데이터 저장한 타입)
nums.extend([11,22,33]) # 연산은 원본 자체가 바뀌지 않음. extend는 원본 자체가 바뀜.
print(f'nums : {len(nums)}개, {nums}')

nums.extend("새해 복 많이 받으세요")
print(f'nums : {len(nums)}개, {nums}')

nums.extend(["새해 복 많이 받으세요"])
print(f'nums : {len(nums)}개, {nums}')

#nums.extend(2024) # 시퀀스가 있거나 또는 반복가능한 데이터만 가능
#print(f'nums : {len(nums)}개, {nums}')

# [9] 리스트를 복사해주는 메서드 => 얕은 복사 copy()
nums.append([100,200])
nums2 = nums.copy()

print(f'nums : {len(nums)}개, {nums}')
print(f'nums2 : {len(nums2)}개, {nums2}')

# nums의 [-1]번 요소의 데이터를 2024로 변경
nums[-2] = 2024
print(f'nums : {len(nums)}개, {nums}')
print(f'nums2 : {len(nums2)}개, {nums2}')

# nums의 -1번 요소의 0번 요소의 데이터를 77로 변ㅇ경
nums[-1][0] = 77

print(f'nums : {len(nums)}개, {nums}')
print(f'nums2 : {len(nums2)}개, {nums2}')