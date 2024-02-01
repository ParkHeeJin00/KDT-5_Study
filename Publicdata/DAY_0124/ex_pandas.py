import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib

weather_df = pd.read_csv('../DATA/daegu-utf8.csv', encoding='utf-8-sig')
print(weather_df.columns)
print(weather_df['날짜'].dtype)	# 날짜 컬럼은 object 타입

# 컬럼명 변경
weather_df.columns= ['날짜','지점','평균기온','최저기온','최고기온']
print(weather_df.columns)

# 날짜 컬럼의 데이터 타입을 datetime 타입으로 변경
weather_df['날짜'] = pd.to_datetime(weather_df['날짜'], format='%Y-%m-%d')
# = weather_df['날짜']=weather_df['날짜'].astype("datetime64[ns]")
print(weather_df['날짜'].dtype)

# 누락값 개수 구하기
print(weather_df.head(5))
print(weather_df.shape)   ## (42704,5)
num_rows = weather_df.shape[0]	 # shape(row, col), shape[0] : row의 개수
num_missing = num_rows - weather_df.count()	# count() : null값 제외한 값의 개수   # 각 컬럼별로 계산
print(num_missing)

# 누락값 처리
weather_df = weather_df.dropna(axis=0)  # 날짜 별로 통째로 삭제
print(weather_df.count())  # 각 컬럼별 개수 반환
print(weather_df.head(5))

# 누락값을 제거한 최종 데이터를 csv파일로 저장
weather_df.to_csv('../DATA/daegu-utf8-df.csv',	index=False,	mode='w',	encoding='utf-8-sig')
# 쓸 데 없는 위치 인덱스를 안 넣겠다

# 특정 연도와 달의 최고,최저 기온 평균값 계산
year_df =weather_df[weather_df['날짜'].dt.year == 2023]
month_df =year_df[year_df['날짜'].dt.month == 8]
print(month_df.head())

# 특정 연도와 달의 최고,최저 기온 평균값 계산
max_temp_mean =	round(month_df['최고기온'].mean(),1)
min_temp_mean =	round(month_df['최저기온'].mean(),1)
print(f'2023년 8월 최저기온 평균:{min_temp_mean},	최고기온 평균 :{max_temp_mean}')


# -----------------------------------------------------------------------------
# 1990년대와 2019년대 최고 기온 비교
# -----------------------------------------------------------------------------

def	draw_two_plots(title,	x_data,	max_temp_list1,	label_y1,	max_temp_list2,	label_y2):
    plt.rcParams['axes.unicode_minus'] = False
    plt.figure(figsize=(10,	4))
    plt.plot(x_data,	max_temp_list1,	marker='s',	markersize=6,	color='b',	label=label_y1)
    plt.plot(x_data,	max_temp_list2,	marker='s',	markersize=6,	color='r',	label=label_y2)
    plt.xticks(x_data)		#	모든 xtick값을 출력함
   #plt.ylim(10,40)
    plt.title(title)
    plt.legend()
    plt.show()
def main():

    search_month = int(input("달을 입력하세요:   "))

    weather_df = pd.read_csv('../DATA/daegu-utf8-df.csv', encoding='utf-8-sig')
    # 타입 캐스팅
    weather_df['날짜'] = pd.to_datetime(weather_df['날짜'], format='%Y-%m-%d')
    # 0의 값이 10개 들어간 리스트 생성
    first_decade_max_temp_list = [0] * 10  # 10년 동안 각 월의 평균 저장
    second_decade_max_temp_list = [0] * 10

    first_decade = 1990
    second_decade = 2010

    for year in range(10):  # 1990~1999 / 2010~2019
        # 1990
        first_decade_df = weather_df[(weather_df['날짜'].dt.year == first_decade + year) & (weather_df['날짜'].dt.month == search_month)]
        first_decade_max_temp_list[year] = round(first_decade_df['최고기온'].mean(), 1)
        # 2010
        second_decade_df = weather_df[(weather_df['날짜'].dt.year == second_decade + year) & (weather_df['날짜'].dt.month == search_month)]
        second_decade_max_temp_list[year] = round(second_decade_df['최고기온'].mean(), 1)

    print(f'{first_decade}년대 {search_month}월 최고 기온 평균:   {first_decade_max_temp_list}')
    print(f'{second_decade}년대 {search_month}월 최고 기온 평균:   {second_decade_max_temp_list}')

    first_decade_high_temp_mean = round(sum(first_decade_max_temp_list) / len(first_decade_max_temp_list), 1)
    second_decade_high_temp_mean = round(sum(second_decade_max_temp_list) / len(second_decade_max_temp_list), 1)

    print(f'{first_decade}년대 {search_month}월 전체 최고 기온 평균:   {first_decade_high_temp_mean}')
    print(f'{second_decade}년대 {search_month}월 전체 최고 기온 평균:   {second_decade_high_temp_mean}')

    x_data = [i for i in range(10)]
  # draw_two_plots(title, x_data, max_temp_list1, label_y1, max_temp_list2, label_y2)
    draw_two_plots(f'{search_month}월 최고 기온 비교', x_data, first_decade_max_temp_list, str(first_decade) + '년대',
                   second_decade_max_temp_list, str(second_decade) + '년대')


main()