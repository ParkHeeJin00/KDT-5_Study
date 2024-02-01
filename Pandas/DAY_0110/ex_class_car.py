# -------------------------------------------------------------------------
# 자동차 관리 프로그램 만들기
# - 엔진, 연료, 브랜ㄷ, 색상, 번호
# - 전진, 후진, 좌회전, 우회전, 정지
# -------------------------------------------------------------------------
engine = '휘발유엔진'
food = '휘발유'
maker = '현대'
color = '흰색'
number = '111가1111'

engine = '휘발유엔진'
food = '휘발유'
maker = '현대'
color = '흰색'
number = '111가2222'

engine = '휘발유엔진'
food = '휘발유'
maker = '기아'
color = '회색'
number = '111가3333'


def go(number):print(f'{number} 자동차가 전진')
def back(number):print(f'{number} 자동차가 후진')
def left_go(number):print(f'{number} 자동차가 좌회전')
def rigt_go(number):print(f'{number} 자동차가 우회전')
def stop(number):print(f'{number} 자동차가 정지')

carDict = {'111가1111' : {'engine':'휘발유엔진','color':'흰색','maker':'현대', 'autodrive':False}
          ,'111가2222' : {'engine':'휘발유엔진','color':'흰색','maker':'기아','autodrive':False}
          ,'111가3333' : {'engine':'경유엔진','color':'녹색','maker':'현대','autodrive':True}
           }
# 자동차 관리 ---------------------------------------------------------
# for k, v in carDict.items():
#     print(f'판매 차량 [{number}]')
#     for subK, subV in v.items():
#         print(f'- {subK} : {subV}')
# --------------------------------------------------------------------
# 자동차 클래스
# - 역할 : 자동차 관련 데이터, 기능을 모두 저장 관리 클래스
# - 문법
#   class 클래스명 :
#    <--> 코드
# --------------------------------------------------------------------
class Car:
    maker = '현대'

    # 클래스 생성 시 필수로 사용되는 메서드
    # 힙 메모리에 속성들의 값을 저장해주는 역할
    def __init__(self,engine_,food_,color_,number_):  ## self가 가지는 것은 힙의 주소값 / 힙의 주소 내에 객체의 속성 저장
        print('__init__')
        # 자동차 클래스가 가지는 속성을 메모리 힙에 저장
        self.engine =engine_
        self.color =color_
        self.food =food_
        self.number =number_

    ## 각각이 가진 속성은 따로 저장 - 메모리때문에 / 각 객체가 가진 정보가 self / 함수를 쓸때, 자동으로 객체 정보를 넣어줌

    def go(self): print(f'{self.number} 자동차가 전진')

    def back(self): print(f'{self.number} 자동차가 후진')

    def left_go(self): print(f'{self.number} 자동차가 좌회전')

    def rigt_go(self): print(f'{self.number} 자동차가 우회전')

    def stop(self): print(f'{self.number} 자동차가 정지')

# 클래스로 자동차 객체 생성 --------------------------------------------------
myCar = Car('휘발유엔진','휘발유','흰색','111가1111')
myCar2 = Car('휘발유엔진','휘발유','핫핑크색','111가7777')

print(type(myCar))  # Car 타입