# ---------------------------------------------------
# 반복문 - 2 while 반복문
# - 반복의 횟수가 정해 지지 않은 경우
# ---------------------------------------------------
# [요청] 사용자가 'x' 입력 전까지 입력 받은 데이터를 저장해주세요
# => 몇 번 입력할 지 알 수 없음 ==> 무한 입력 받기
# => 종료 조건 ==> 사용자 'x' 입력

# while True:    ## while 1:   but 가독성을 위해 True 사용
#     data = input("저장하고 싶은 데이터 입력 (종료 x) : ")
#     # 종료 검사 => break : 키워드가 있는 부분에서 바로 반복 종료, 아래 코드 실행 안됨
#     if data == 'x' or data == 'X':
# #   if data in ('x', 'X'):    # ( ) x와 X를 튜플로 인지 -> 각자가 하나의 데이터 data와 각 데이터가 완전히 일치해야함
#         break                 # str이면 각각의 원소로 보는게 맞지만 위는 튜플로 인지
#         print('ok')   # 실행 안함
# print("프로그램 종료")

# ---------------------------------------------------
# [요청] 사용자로부터 x/X 입력 전까지 계속 정수를 입력
#       입력 받은 정수 만큼 알파벳을 출력
# [예시] 출력 원하는 알파벳 수 입력 : 5
#        abcde
#       출력 원하는 알파벳 수 입력 : 1
#        a
#       출력 원하는 알파벳 수 입력 : 27
#        abcdefghijklmnopqrstuvwxyz
# ---------------------------------------------------
# while True:
#     num = input("출력 원하는 알파벳 수 입력 : ")
#
#     # 무한 입력 반복 종료 조건
#     if num in ('x', 'X'):
#         print("종료입니다.")
#         break       # 즉시 종료
#     int(num)
#     aCode = ord('a')   # chr(97)   ## 대문자를 원하면 ord('A')
#     for value in range(5):
#         value += aCode
#         print(f'value => {value}, {chr(value)}')


# while Ture:
#     count = input("출력 원하는 알파벳 수 : ")
#     # 종료 코드
#     if count in ('x', 'X'):
#         print("프로그램 종료")
#         break          ## 가장 가까이 있는 반복문인 while문을 빠져나감
#
#     if count.isdecimal():
#         count = int(count)
#         aCode = ord('A')
#         for value in range(count):
#             value += aCode
#
#             print(f'value => {value}, {chr(value)}')
#
#             if value == ord('Z'): break   ## 가장 가까이 있는 반복문인 for문만 빠져나감
#
#     else:
#         print("정확한 데이터가 아닙니다.")
#
# print("-------코드 끝 부분 -------")


isEnd = False       ## flag 변수

for n in range(100):

    if isEnd:
        print("프로그램 종료합니다.")
        break

    print(f"out -> {n}")

    for n2 in range(100):
        if n2>10:
            isEnd = True
            break   ## 가장 가까운 for문만 종료
        print(f"in -> {n2} =====>{n}번째")


# [요청] 내부의 반복문에서 데이터가 10초과되면 프로그램을 종료 --------
n= 1
isEnd = False

while n <= 100:
    # 종료 조건
    if isEnd:
        print("프로그램 종료합니다.")
        break
    print(f'out -> {n}')
    # 내부 while
    n2 = 1    ## 안에서만 쓰는 변수니까 안에 넣기
    while n2<=100:
        if n2 > 10:
            print("내부 while문 종료")
            isEnd = True
            break
        print(f'in -> {n2} =====>{n}번째')
        n2 += 1
    n += 1
