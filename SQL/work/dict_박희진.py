def conDict():

    contry = {'Seoul':['South Korea','Asia',9655000],
              'Tokyo':['Japan','Asia',14110000],
              'Beijing':['China','Asia',21540000],
              'London':['United Kingdom','Europe',14800000],
              'Berlin':['Germany','Europe',3426000],
              'Mexico City':['Mexico','America',21200000]}

    while True:
        print('''-------------------------------------
1. 전체 데이터 출력
2. 수도 이름 오름차순 출력
3. 모든 도시의 인구순 내림차순 출력
4. 특정 도시의 정보 출력
5. 대륙별 인구수 계산 및 출력
6. 프로그램 종료
-------------------------------------''')
        n = int(input('메뉴를 입력하세요:'))
        if n == 6:
            print('프로그램을 종료합니다.')
            break

        idx = 1
        if n == 1:
            for k,v in contry.items():
                print(f'[{idx}] {k}: {v}')
                idx +=1

        if n == 2:
            contrySort = dict(sorted(contry.items(), key = lambda x:x[0]))

            for k,v in contrySort.items():
                print(f'[{idx}] {k:<13}:', end = ' ')
                print(f'{v[0]:<17}{v[1]:<12}{v[2]:>10,}')
                idx += 1

        if n == 3:
            contrySort = dict(sorted(contry.items(), key = lambda x:x[1][2], reverse = True))
            for k,v in contrySort.items():
                print(f'[{idx}] {k:<13}:{v[2]:>13,}')
                idx += 1

        if n == 4:
            name = input('출력할 도시 이름을 입력하세요.')
            if name in contry.keys():
                print(f'도시:{name}\n국가:{contry[name][0]}, 대륙:{contry[name][1]}, 인구수:{contry[name][2]:,}')
            else:
                print(f'도시이름: {name}은 key에 없습니다.')

        if n ==5:
            name = input('대륙 이름을 입력하세요(Asia, Europe, America)')
            sum = 0
            for k in contry.keys():
                if name == contry[k][1]:
                    print(f'{k}: {contry[k][2]:,}')
                    sum += contry[k][2]

            print(f'{name} 전체 인구수: {sum:,}')


conDict()