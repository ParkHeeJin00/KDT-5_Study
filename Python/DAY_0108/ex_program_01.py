# ---------------------------------------------------------------
# 나의 프로그램 - 계산기
# [ 계산기 ]
# 1. 입력
# 2. 덧셈
# 3. 뺄셈
# 4. 곱셈
# 5. 나눗셈
# 6. 기록보기
# 7. 검색
# 8. 삭제
# 9. 종료
# ---------------------------------------------------------------
# 사용자 정의 함수 -------------------------------------------------
# 함수 기능 : 연산 결과 리스트에서 검색어에 해당하는 데이터만 출력
# 함수 이름 : seachResult
# 매개 변수 : seach
# 함수 결과 : None
# ---------------------------------------------------------------
def seachResult(seach):
    cnt = 0
    for calc in calcList:
        if seach in calc:
            print(calc)
            cnt +=1
        else:
            print("찾을 수 없는 기록입니다.")
    print(f'{cnt}개 검색 결과가 있습니다.' if cnt else '검색결과가 없습니다.')

# 계산 기록 저장할 전역 변수 선언 ------------------------------------
calcList = []

while True:
    print("[ 나의 계산기 ]")
    print('1. 입력 ')
    print('2. 덧셈 ')
    print('3. 뺄셈 ')
    print('4. 곱셈 ')
    print('5. 나눗셈 ')
    print('6. 기록보기 ')
    print('7. 검색 ')
    print('8. 삭제 ')
    print('9. 종료 ')
    choice = input('메뉴 선택 : ')
    if choice.isdecimal():
        if choice == '1':
            data = input('2개 정수 (예:10 20)')
            n1, n2 = list(map(int,data.split()))
        elif choice == '2':
            calcList.append(f'덧셈 결과 : {n1} + {n2} = {n1+n2}')
            print(f'{calcList[-1]}\n')
        elif choice == '3':
            calcList.append(f'뺄셈 결과 : {n1} - {n2} = {n1-n2}')
            print(f'{calcList[-1]}\n')
        elif choice == '4':
            calcList.append(f'곱셈 결과 : {n1} * {n2} = {n1*n2}')
            print(f'{calcList[-1]}\n')
        elif choice == '5':
            calcList.append(f'나눗셈 결과 : {n1} / {n2} = {n1/n2 if n2 else "0으로 나눌 수 없습니다."}')
            print(f'{calcList[-1]}\n')
        elif choice == '6':
            print('==> 계산 기록 출력')
            calcList.sort(reverse=True)
            for calc in calcList:
                print(calc)
            print("=========================")
        elif choice == '7':
            seach = input("검 색 : ")
            seachResult(seach)
        elif choice == '8':
            clearResult = input('정말 모든 데이터가 사라지는데 지우겠습니까? Y/N ')
            if clearResult == 'Y':
                calcList.clear()
                print("모든 데이터를 삭제하였습니다.")
            elif clearResult == "N":
                print('삭제하지 않았습니다.')
            else:
                print("Y 또는 N을 입력하세요.")
        elif choice == '9':
            print("프로그램 종료합니다.")
            break
        else:
            print("메뉴는 1~6 선택 가능합니다.")
    else:
        print("없는 메뉴입니다.")
