class person:
    def __init__(self):
        self.hello = '안녕하세요'

    def greeting(self):
        print(self.hello)

person().greeting()

# 34.5
class Knight:
    def __init__(self,health,mana,armor):
        self.health = health
        self.mana = mana
        self.armor = armor

    def slash(self):
        print('베기')

# 34.6
class Annie:
    def __init__(self,health, mana, ability_power):
        self.health=health
        self.mana=mana
        self.ability_power=ability_power

    def tibber(self):
        print(f'티버: 피해량 {self.ability_power * 0.65 + 400}')

health, mana, ability_power = map(float, input().split())

x = Annie(health=health, mana=mana, ability_power=ability_power)
x.tibber()

# 35.5
class Date:

    @staticmethod
    def is_date_vaild(date):
        year, month, day = map(int, date.split('-'))
        return 0<month<=12 and 0< day <=31

if Date.is_date_vaild('2000-10-31'):
    print('올바른 날짜 형식입니다.')
else:
    print('잘못된 날짜 형식입니다.')

# 35.6
class Time:
    def __init__(self,hour,minute,second):
        self.hour = hour
        self.minute = minute
        self.second = second

    @classmethod
    def is_time_vaild(cls, str):
        cls.hour, cls.minute, cls.second = map(int, str.split(':'))
        return 0<cls.hour<=24 and 0<cls.minute<=59 and 0<cls.second<=60

    @classmethod
    def from_string(self):
        return Time(self.hour, self.minute, self.second)


time_string = input()

if Time.is_time_vaild(time_string):
    t = Time.from_string(time_string)
    print(t.hour,t.minute,t.second)
else:
    print('잘못된 시간 형식입니다.')

# 36.8
class AdvancedList(list):

    def replace(self,old, new):
        while old in self:
            self[self.index(old)] = new

x = AdvancedList([1,2,3,1,2,3,1,2,3])
x.replace(1,100)
print(x)

# 36.7
class Animal:
    def eat(self):
        print('먹다')

class Wing:
    def flap(self):
        print('파닥거리다')

class Bird( Animal, Wing):
    def __init__(self):
        pass

    def fly(self):
        print('날다')

b = Bird()
b.eat()
b.flap()
b.fly()
print(issubclass(Bird,Animal))
print(issubclass(Bird,Wing))