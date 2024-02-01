import pandas as pd
import matplotlib.pyplot as plt


# df 불러오기
df = pd.read_excel(r'../DATA/subway.xls', sheet_name='지하철 시간대별 이용현황', header = [0,1]) # 멀티 인덱스
print(df.head())
print(df.columns)

commute_time_df = df.iloc[ :, [1,3,10,12,14]]  # 호선 및 지하철역명 + 출근 시간대 승차 컬럼만 뽑아오기
print(commute_time_df.dtypes)   # 승차 type : object / 숫자로 타입변환 해야함

# , 없애기
commute_time_df[('07:00:00~07:59:59', '승차')] = commute_time_df[('07:00:00~07:59:59', '승차')].apply(lambda x : x.replace(',',''))
commute_time_df[('08:00:00~08:59:59', '승차')] = commute_time_df[('08:00:00~08:59:59', '승차')].apply(lambda x : x.replace(',',''))
commute_time_df[('09:00:00~09:59:59', '승차')] = commute_time_df[('09:00:00~09:59:59', '승차')].apply(lambda x : x.replace(',',''))
# commute_time_df.replace(',','', inplace = True)

# astype은 Sr의 값의 타입을 변환하는 함수
commute_time_df = commute_time_df.astype({('07:00:00~07:59:59', '승차'):'int64'})
commute_time_df = commute_time_df.astype({('08:00:00~08:59:59', '승차'):'int64'})
commute_time_df = commute_time_df.astype({('09:00:00~09:59:59', '승차'):'int64'})

print(commute_time_df.dtypes)

# 각 행(지하철 역)의 승차 인원 수 합 계산
row_sum_df = commute_time_df.sum(axis=1, numeric_only=True)
passenger_number_list =	row_sum_df.to_list()
print(row_sum_df)

# 최대 승차 수를 가지는 지하철 역 찾기
max_number = row_sum_df.max(axis=0)	#	해당 열에서 최대값 찾기
max_number

# 최대 승차 수를 가지는 행의 인덱스 구하기
max_index = row_sum_df.idxmax()
max_line, max_station = df.iloc[max_index, [1,3]]  # [1] : 호선 / [3] : 지하철역명
print(f'출근 시간대 최대 승차 인원역 : {max_line} {max_station} {max_number:,}')

# 그래프 그리기
passenger_number_list.sort(reverse = True)
plt.figure(dpi = 100)
plt.bar(range(len(passenger_number_list)), passenger_number_list)
plt.show()

