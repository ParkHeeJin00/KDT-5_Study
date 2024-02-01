import csv
import matplotlib.pyplot as plt
import  platform
import koreanize_matplotlib


def	draw_piechart(city_name, city_population, voting_population):

    non_voting_population = city_population - voting_population
    population = [non_voting_population, voting_population]
    color = ['tomato',	'royalblue']
    plt.pie(population,	labels=['18세 미만',	'투표가능인구'], autopct='%.1f%%' , colors=color, startangle=90)
    plt.legend(loc = 1)
    plt.title(city_name + "	투표 가능 인구 비율")
    plt.show()


def get_voting_population(city):

    f = open('../DATA/age.csv', encoding='utf-8-sig')
    data = csv.reader(f)
    next(data) # 헤더 정보 건너뜀
    voting_number_list = []
    city_name = ''
    city_population = 0 # 도시 전체 인구수
    voting_population = 0
    # 전체 데이터 보기
    for row in data:
        if city in row[0]:
            city_population = row[1]   # row[1] : 총 인구수

            # 도시 전체 인구수에서 천단위 콤마 제거
            if ',' in city_population:
                city_population = city_population.replace(',', '')

            city_population = int(city_population)
            city_name = row[0]

            # 필요한 나이 데이터 보기
            for data in row[21:]: # 18세 이상
                if ',' in data:
                    data = data.replace(',','') # 천단위 콤마 제거
                voting_num = int(data)
                # 각 연령대별 투표 인구수를 리스트에 추가
                voting_number_list.append(voting_num)
                # 누적된 투표 가능 인구수
                voting_population += voting_num
            break # 제일 먼저 나오는 데이터만 분석하기 위해
    f.close()

    print(f'{city_name}전체 인구수:{city_population:,}명,투표 가능 인구수: {voting_population:,}명')
    draw_piechart(city_name, city_population, voting_population)

city = input('투표 가능 인구수를 확인할 도시이름을 입력하시오: ')
get_voting_population(city)