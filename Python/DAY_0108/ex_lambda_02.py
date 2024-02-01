# 리스트 안에 모든 원소를 더한 합계를 출력
datas = ['1','4','9']

# => 반복문 사용
for idx, d in enumerate(datas):
    datas[idx] = int(d)

# => 내장함수 map()
datas = list(map(int,datas))

# => 원소에 *100한 값을 리스트에 저장하기
# 사용자 정의 함수 사용
def multValue(x):
    return x*100
datas = list(map(multValue,datas))

# 람다 함수 사용
datas100 = list(map(lambda x:x*100, datas))
print(datas100)

def greeting():
    print('반갑습니다.~')

# 람다 함수에서 매개변수가 없는 경우
print( (lambda :print('반갑습니다.~'))() )
