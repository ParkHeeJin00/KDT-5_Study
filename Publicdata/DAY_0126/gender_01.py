import csv
import matplotlib.pyplot as plt
import platform
import koreanize_matplotlib
def print_population(population):

    for i in range(len(population)):
        print(f'{i:3d}세: {population[i]:4d}명', end=' ')
        if (i + 1) % 10 == 0:
            print()
    print()


def draw_geneder_population(title, male_num_list, female_num_list):
    if platform.system() == 'Windows':
        plt.rc('font', family='Malgun Gothic')
    else:
        plt.rc('font', family='AppleGothic')
# barh(y축 범위, data)
    plt.barh(range(len(male_num_list)), male_num_list, label='남성')
    plt.barh(range(len(female_num_list)), female_num_list, label='여성')
    plt.rcParams['axes.unicode_minus'] = False
    plt.title(title + ' 성별 인구 비율')
    plt.legend()
    plt.show()

	
def calculate_population():
    f = open('../DATA/gender.csv', encoding='utf-8-sig')
    data = csv.reader(f)
    male_num_list =[]
    female_num_list =[]

    district = input('시군구 이름을 입력하세요: ')
    for row in data:
        if district in row[0]:
            for male in row[106:207]:
                if','in male:
                    male=male.replace(',','')
                male_num_list.append(-int(male))  # 남성의 값을 음수로 하면 됨
            for female in row[209:310]:
                if','in female:
                    female=female.replace(',','')
                female_num_list.append(int(female))
            break
    f.close()
    print(f'남성 총 인구수:{sum(male_num_list):,} ')
    print_population(male_num_list)
    print('-------------------------------')
    print(f'여성 총 인구수:{sum(female_num_list):,} ')
    print_population(female_num_list)
    draw_geneder_population(district, male_num_list, female_num_list)

calculate_population()



