## DAY_1 과제

### 1번 문제의 컴퓨팅 사고 과정

1. 날짜 컬럼 datetime으로 변경
2. 하나의 월의 일교차 구하기
3. 월의 일교차 평균값이 최고값일 때, 월과 값 저장하기
4. 해당 년도의 일교차 평균값이 최고 월과 해당 년도 xlist에 저장하기
5. 최고값을 ylist에 저장하기
6. 년도마다 반복하기
7. xlist → 년도.월 
8. ylist → 최고값

### 1번

```python
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
```

![image](https://github.com/ParkHeeJin00/KDT-5_Study/assets/155441547/ee631cb0-1513-4d1b-9142-9956fca2ab64)

## DAY_2 과제

### 1번 문제의 컴퓨팅 사고 과정

1. 1~7번 노선만 뽑아서 DF 생성
2. 7시 하차와 8시 하차를 더 해서 총 하차 컬럼 추가
3. 노선을 인덱스로 setting
4. 각 노선의 총 하차 중 가장 큰 값을 가진 row의 총 하차값을 y리스트에 추가
5. row의 하차역 xlist에 추가
6. bar 그래프 생성

### 1번

'''python
subDF = pd.read_csv('../DATA/subwaytime.csv',usecols=[1,3,11,13], header=0, names=['노선명','지하철명','7시 하차','8시 하차'])
subDF.dropna(inplace=True)

hosubDF = subDF[subDF['노선명'].isin(['1호선','2호선','3호선','4호선','5호선','6호선','7호선'])]
hosubDF['7시 하차'] = hosubDF['7시 하차'].astype('int64')
hosubDF['8시 하차'] = hosubDF['8시 하차'].astype('int64')
hosubDF.set_index('노선명', inplace=True)

yList = []
xList = []

for i in hosubDF.index.unique():
    wantDF = hosubDF.loc[i]
    wantDF['총 하차'] = wantDF['7시 하차'] + wantDF['8시 하차']
    a = wantDF.sort_values(by = '총 하차', ascending=False).iloc[0]
    xList.append(f'{i} {a[0]}')
    yList.append(a[3])
for i in range(7):
    print(f'출근 시간대 {i+1}호선 최대 하차역: {xList[i][4:]}역, 하차인원: {yList[i]:,}명')
    
# 그래프 그리기
plt.figure(figsize=(10,5))
plt.bar(xList,yList)
plt.title('출근 시간대 지하철 노선별 최대 하차 인원 및 하차역')
plt.xticks(rotation = 80)
'''

![image](https://github.com/ParkHeeJin00/KDT-5_Study/assets/155441547/447cc699-f875-422b-83a8-01bf13bbcee3)
