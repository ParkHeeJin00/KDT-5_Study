#--------------------------------------------------------
# 전역 변수(Global Variable)와 지역 변수(Local Variable)
# # 전역 변수(Global Variable)
#   - 파이썬(py) 파일에 존재 하는 변수
#   - 파일 내부 모든 곳에서 사용 가능한 변수
#   - 파일 실행을 종료하면 메모리에서 사라짐
# # 지역 변수(Local Variable)
#   - 함수에 존재 하는 변수
#   - 함수에서만 사용 가능한 변수
#   - 함수가 종료 되면 변수들은 메모리에서 사라짐
#--------------------------------------------------------
# 사용자 정의 함수 -----------------------------------------
def currentDate(year,month,day):
    # year, month, day => 지역 변수
    print(f'Today : {year}/{month:0>2}/{day:0>2}')

def currentDate2(month, day):
    # month, day => 지역 변수
    # year => 전역 변수    ## 함수 내에 존재X 파일에서 찾게 됨
    print(f'Today : {year}/{month:0>2}/{day:0>2}')


def currentDate3(month, day,week):
    # month, day => 지역 변수
    # year => 전역 변수    ## 함수 내에 존재X 파일에서 찾게 됨
    print(f'Today : {year}/{month:0>2}/{day:0>2}/{week}')


# 전역 변수 ------------------------------------------------
year, month, day = 2024,1,8

# 함수 사용 즉 함수 호출
currentDate3(month ,day, "Friday")

# 변수 값 확인 출력
print(f'year : {year}, month : {month}, day : {day}')

# 함수의 변수인 지역 변수는 함수 밖에서 사용 불가
# print(f'week : {week}')