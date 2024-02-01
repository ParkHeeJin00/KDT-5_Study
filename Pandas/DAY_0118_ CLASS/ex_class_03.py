# ------------------------------------------------------------
# 2차원 점 클래스
# 클래스 이름: pint2D
# 클래스 속성: x,y, color, shape, size
# 클래스 기능: 그리기, 지우기 ,정보 출력
# ------------------------------------------------------------
# import ex_class_02 as e2  ## 이중 상속 가능
class point2D:
    # 클래스 속성 => 없음

    # 객체 즉 인스턴스 생성
    def __init__(self,x,y,color,shape,size):
        self.x = x
        self.y = y
        self.color = color
        self.shape = shape
        self.size = size

    # 객체 즉 인스턴스 메서드
    def draw(self):
        print(f'좌표 ({self.x},{self.y})에 {self.shape} 그리기')

    def printInfo(self):
        print('2D')
        print(f'위치 : ({self.x}, {self.y})')
        print(f'색상 : {self.color}')
        print(f'형태 : {self.shape}')


# ------------------------------------------------------------
# 3차원 점 클래스
# 클래스 이름: pint3D
# 클래스 속성: x,y, z, color, shape, size
# 클래스 기능: 그리기, 지우기 ,정보 출력
# ------------------------------------------------------------
class point3D(point2D):
    # 클래스 속성 => 없음

    # 객체 즉 인스턴스 생성
    def __init__(self,x,y,z,color,shape,size):
        # 부모 객체 생성
        super().__init__(x,y,color,shape,size)
        self.z = z    ## 부모 객체로부터 상속받지 않고 자녀 클래스가 가지는 속성 생성
        print('point3D')

    # 상속받은 부모의 메서드를 나의 취향에 맞게 수정 => 오버라이딩 (상속관계에서 가능)
    def printInfo(self):
        print('3D')
        print(f'위치 : ({self.x}, {self.y}, {self.z})')
        print(f'색상 : {self.color}')
        print(f'형태 : {self.shape}')

p2 = point2D(10,10,'red','circle',(10,10))
p3 = point3D(5,5,5,'yellow','rectangle',(3,3,3))
print(p3.x,p3.y,p3.color,p3.size)

p3.printInfo()

# import ex_class_02 as e2
#
# class freeRidingCas(e2.Car):
#
#     def __init__(self,wheel,color,number,kind,mode):
#
#         super().__init__(wheel,color,number,kind)
#         self.mode = mode
#
#         def driving(self,where):
#             print(f'{where}에 {self.number} 차가 드라이브하고 있다.')
#
#         def stop(self, place):
#             print(f'{self.number} 차가 {place}에 정지한다.')
#
#         def back(self):
#             print(f'{self.number} 차가 후진한다.')
#
#     # 객체 즉 인스턴스 생성
#     def __init__(self,x,y,z,color,shape,size):
#         # 부모 객체 생성
#         super().__init__(x,y,color,shape,size)
#         self.z = z    ## 부모 객체로부터 상속받지 않고 자녀 클래스가 가지는 속성 생성
#         print('point3D')
#
#     # 상속받은 부모의 메서드를 나의 취향에 맞게 수정 => 오버라이딩 (상속관계에서 가능)

