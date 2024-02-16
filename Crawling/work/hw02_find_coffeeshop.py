import pandas as pd

shopDF = pd.read_csv('../work/holly_branches.csv', encoding='utf-8', header=0, index_col=0)

while True:
    city = input('검색할 매장의 도시를 입력하세요:')
    if city == 'quit':
        print('종료 합니다.')
        break

    citylist = []
    for i in shopDF.index:
        if city in shopDF.loc[i, '위치(시/구)']:
            citylist.append([shopDF.loc[i, '주소'], shopDF.loc[i, '전화번호']])

    print('-' * 30, f'검색된 매장수: {len(citylist)}', '-' * 30, sep='\n')
    for n, i in enumerate(citylist):
        print(f"[{n + 1}]: {i}")
    print('-' * 90)
