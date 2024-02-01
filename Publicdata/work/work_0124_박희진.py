import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib

# 1번
def work1():

    weatherDF = pd.read_csv('DATA/daegu-utf8-df.csv', encoding='utf-8-sig')
    weatherDF['날짜'] = weatherDF['날짜'].astype('datetime64[ns]')
    
    currentYear = 2014

    decadeDF = weatherDF[(weatherDF['날짜'].dt.year.between(currentYear,currentYear+10))]

    yL = []
    xList = []
    for y in range(currentYear,currentYear+10):
        mL = {}
        for m in range(1,13):
            wantDF = decadeDF[(decadeDF['날짜'].dt.year == y) & (decadeDF['날짜'].dt.month == m)]
            mL[m] = (wantDF['최고기온']-wantDF['최저기온']).mean()
            
        yL.append(max(mL.values()))
        xList.append(f'{y}.{max(mL,key=mL.get)}')

    plt.figure(figsize=(11,5))
    plt.bar(xList,yL)
    plt.title('지난 10년간 대구의 일교차가 가장 큰 달')
    plt.xlabel('Year/Month')
    plt.ylabel('일교차')
    plt.show()
work1()

# 2번
def work2():
    weatherDF = pd.read_csv('DATA/daegu-utf8-df.csv', encoding='utf-8-sig')
    weatherDF['날짜'] = weatherDF['날짜'].astype('datetime64[ns]')

    startyear = int(input('시작 연도를 입력하세요: '))
    lastyear = int(input('마지막 연도를 입력하세요: '))
    mon = int(input('기온 변화를 측정할 달을 입력하세요: '))

    # 최고/최저 기온 구하기
    max_temp = []
    min_temp = []
    xlist = [i for i in range(startyear, lastyear+1)]
    for i in range(startyear, lastyear + 1):
        temDF = weatherDF[(weatherDF['날짜'].dt.year == i) & (weatherDF['날짜'].dt.month == mon)]
        max_temp.append(round(temDF['최고기온'].mean(),1))
        min_temp.append(round(temDF['최저기온'].mean(),1))

    print(f'{startyear}년부터 {lastyear}년까지 {mon}월의 기온 변화')
    print(f'{mon}월 최저기온 평균:')
    print(*min_temp, sep=', ')
    print(f'{mon}월 최고기온 평균:')
    print(*max_temp, sep=', ')
   
    
    plt.figure(figsize=(16,4))
    plt.rc('axes',unicode_minus = False)
    plt.plot(xlist, min_temp,'b-s', label = '최저기온')
    plt.plot(xlist, max_temp,'r-s', label = '최고기온')
    plt.title(f'{startyear}년부터 {lastyear}년까지 {mon}월의 기온 변화')
    plt.legend()
    plt.xticks(xlist)
    plt.show()
    
work2()




