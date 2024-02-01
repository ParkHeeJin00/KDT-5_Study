# ----------------------------------------------------
# 다양한 함수의 형태 - 특별한 함수 (2)
# - 매개변수의 갯수를 유동적으로 가변으로 하는 함수
# - 키와 값의 덩어리 데이터
# - 형태 : def 함수명( **data ):
# - 가변 인자 함수
# - 매개변수 갯수 : 0개 ~ n개
# - 호출 : 함수명(키1=값1)        ## 키는 변수명 - '' X
#         함수명(키1=값1, 키2=값2,...,키n=값n)
#         함수명()
# ----------------------------------------------------
aDict = {'name':'Hong', 'age' : 10}
aDict.update(job ='학생')
aDict.update(job ='학생', birth = '1112', blood = 'A') ## update는 가변 인자 함수
print(aDict)

## p375 - 독스트링 : 함수에 대한 설명
def add(a,b):
    '''

    :param a: int
    :param b: int
    :return: a+b int
    '''
    return a,b

add( 10, 2 )

# ----------------------------------------------------
# 함수 기능 : 회원 가입 기능
# 함수 이름 : joinMember
# 매개 변수 : 이름, 전화 번호, 아이디, 이메일, 취미, 주소, 생일,....
#           가변 + 데이터 정보 함께
#           키워드 파라미터 **member
# 반 환 값 : '가입 완료 되었습니다.' str
# ----------------------------------------------------
def joinMember(**member):
    # 멤버 저장소에 멤버 추가 하기
    #mList.append(member)
    members[f'M{len(members)}']=member
    #members.update(**member)   # update가 요구하는 데이터 타입을 충족하기 위해서 언팩킹 ( ** -> 데이터 -> 키 = 값 )

# -----------------------------------------------------------------------
# 함수 사용 즉 함수 호출
# -----------------------------------------------------------------------
# 가입된 회원들 저장 변수
members = {}
mList = []

print(f'[BF] : {members}')
# 회원가입 기능 함수 호출
joinMember(name = 'Hong', age = 17, birth = '2020')
joinMember(id = 'Hong84', phone = '010', job = 'actor', blood = 'B')
joinMember(id = 'baby', birth = '2024', blood = 'A')

print(f'[AF] : {members}')


# ----------------------------------------------------
# 함수 기능 : 회원 가입 기능
# 함수 이름 : joinMember2
# 매개 변수 : 필수 =>id, pw
#           선택 => **option 이름, 전화 번호, 아이디, 이메일, 취미, 주소, 생일,....    ## dict 타입
#           필수를 앞에 적고 선택을 뒤어 적어라 ex) 아래
#           가변 + 데이터 정보 함께
#           키워드 파라미터 **member
# 반 환 값 : '가입 완료 되었습니다.' str
# ----------------------------------------------------
def joinMember2(id,pw, **option):
    # 멤버 저장소에 멤버 추가하기
    print('ok')

# -----------------------------------------------------------------------
# 함수 사용 즉 함수 호출
# -----------------------------------------------------------------------
# 가입된 회원들 저장 변수
members = {}
mList = []

print(f'[BF] : {members}')

# 회원가입 기능 함수 호출
joinMember2('h','ph')
#joinMember2(id = 'Hong84', phone = '010', job = 'actor', blood = 'B')
#joinMember2(id = 'baby', birth = '2024', blood = 'A')

print(f'[AF] : {members}')

# ----------------------------------------------------
# 함수 기능 : 회원 가입 기능
# 함수 이름 : joinMember3
# 매개 변수 : 필수 =>id, pw, loc, gender
#           선택 => **option 이름, 전화 번호, 아이디, 이메일, 취미, 주소, 생일,....
#           순서 => (필수 변수(디폴트 값이 있는 변수는 뒤로), * 변수, ** 변수)
#           키워드 파라미터 **member : 가변 + 데이터 정보 함께
# 반 환 값 : '가입 완료 되었습니다.' str
# ----------------------------------------------------
def joinMember3(id,pw, loc='내국인', gender='남자', **option):  ## 디폴트 값
    # 멤버 저장소에 멤버 추가하기
    ## id가 key, 나머지가 value  ex){'id' : {option : 값}}
    # 키 => id
    # 값 => pw, loc='내국인', gender='남자', **option   # dict 타입으로 담아야 함
    #      {'pw':'123','loc'='내국인', 'gender'='남자', 'etc' : {option} }
    valueDict = {}     # value값을 dict로 제작
    valueDict['pw']= pw
    valueDict['loc']= loc
    valueDict['gender']= gender
    valueDict['etc']= option
    members[id]= valueDict     ## key : id / value : valueDict  # key가 id인 dict의 value 값을 dict로 받음


# -----------------------------------------------------------------------
# 함수 사용 즉 함수 호출
# -----------------------------------------------------------------------
# 가입된 회원들 저장 변수

print(f'[BF] : {members}')

# 회원가입 기능 함수 호출
joinMember3('h1','ph')
joinMember3('h2','ph',gender ='여자')
joinMember3('h3','ph', phone = '010', job = 'actor', blood = 'B')
#joinMember2(id = 'baby', birth = '2024', blood = 'A')

print(f'[AF] : {members}')
for m in members.items():
    print(m)


