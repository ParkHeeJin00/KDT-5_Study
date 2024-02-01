# ----------------------------------------------------------------------------------------
# 자동차 클래스
# 클래스 이름 : Car
# 클래스 속성 : 바퀴, 색상, 차번호, 차종류 => 인스턴스 속성 /  제조사 => 클래스 속성
#               12 , 빨강, 1111,  세단,   현대  
#               12 , 빨강, 2222,  세단,   현대 
# 클래스 기능 : 주행, 정차, 후진
# ----------------------------------------------------------------------------------------
class Car:
    # 클래스 속성
    maker = '현대'

    # 생성자 메서드 => 객체 즉, 인스턴스 생성 메서드
    def __init__(self,wheel,color,number,kind):
        # 힙 영역에 저장
        self.wheel = wheel
        self.color = color
        self.number = number
        self.kind = kind

    # 객체 즉, car 인스턴스 메서드
    def driving(self, where):
        print(f'{where}에 {self.number} 차가 혼자 드라이브하고 있다.')
    def stop(self, place):
        print(f'{self.number} 차가 {place}에 정지한다.')
    def back(self):
        print(f'{self.number} 차가 후진한다.')


# ----------------------------------------------------------------------------------------
# 자동차 인스턴스 생성
# ----------------------------------------------------------------------------------------
myCar = Car(19,'red','1111','세단')
secondCar = Car(20, 'hotpink', '7777','SUV')


# ----------------------------------------------------------------------------------------
# 사랑 클래스
# 클래스 이름 : love
# 클래스 속성 : kind, who
# 클래스 기능 : 행복하다, 슬프다, 그립다
# ----------------------------------------------------------------------------------------
class love:

    # 생성자 메서드
    def __init__(self, kind,who):
        self.kind = kind
        self.who = who

    # love 인스턴스 메서드
    def happy(self):
        print('사랑은 행복한 것')
    def miss(self):
        print('너무 그리웡')

    # 비공개 메서드
    @property
    def sad(self):
        print(f'사랑은 슬픈 것')


# ----------------------------------------------------------------------------------------
# 계산기 클래스
# 클래스 이름 : calc
# 클래스 속성 : 브랜드, 종류, 색상, 크기, 가격
# 클래스 기능 : 덧셈, 뺄셈, 곱셈, 나눗셈
# ----------------------------------------------------------------------------------------
class Calc:
    #클래스 변수
    maker = 'Casio'
    __size = (7,15)  # 비공개 속성 __속성명 : 클래스 밖에서 속성 읽거나/쓰기 불가

    # 객체 즉 인스턴스 생성 메서드
    def __init__(self, kind, color, price,info):
        self.kind = kind
        self.color = color
        self.price = price
        self.__info = info    # 인스턴스 생성 시 계산기에 각인
        self.data = 0

    # 비공개 인스턴스 속성 읽기/쓰기 (getter/setter) 메서드
    def getInfo(self):
        return self.__info
    def setInfo(self,info):
        self.__info = info

    # 비공개 인스턴스 속성 읽기/쓰기 (getter/setter) 메서드
    # => 속성 읽기/쓰기 방식으로 동작하도록 설정 ( 괄호 없이 인식 가능 )
    @property
    def info(self):return self.__info

    @info.setter   # 위 property info의 setter
    def info(self,info):
        self.__info = info

    # 덧셈 기능
    def plus(self, nums):
        self.data += nums
    
    # 나눗셈 기능
    def pdiv(self, nums):
        if not nums:'0으로 나눌 수 없습니다.'
        self.data /= nums

    
    # 뺄셈 기능
    def minus(self, nums):
        self.data -= nums
    
    # 곱셈 기능
    def multi(self, nums):
        self.data *= nums

    # 출력 기능
    def plus(self, nums):
        return self.data
    


# ----------------------------------------------------------------------------------------
# Calc 클래스 인스턴스 생성 => 힙에 생성 : 인스턴스 변수 + 클래스 변수
#                                        인스턴스 메서드 사용 가능
# ----------------------------------------------------------------------------------------
c1 = Calc('공학용','블랙', 10000,'홍길동계산기')

# 인스턴스 속성 읽기 => 공개 속성만 읽기 가능
print(c1.data, c1.color)

# 인스턴스 속성 변경 => 공개 속성만 읽기 가능
c1.color = '빨간색'

# 인스턴스 비공개 속성 읽기 => 전용 메서드 getter 통해서 읽기
print(c1.getInfo(), c1.info)   # c1.info - 속성을 읽는것 같지만 info 메서드가 실행된 것

# 인스턴스 비공개 속성 변경 => 전용 메서드 setter 통해서 쓰기
c1.setInfo('내계산기') 
c1.info = '내계산기'

print(c1.getInfo(), c1.info)
# ----------------------------------------------------------------------------------------
# Calc 클래스로 계산기 정보 확인 => 클래스 변수만 확인 가능(객체 생성 전까지)
#                                 인스턴스 변수나 메서드 사용 불가능!! ( self 값이 없음)
# ----------------------------------------------------------------------------------------
print(Calc.maker)