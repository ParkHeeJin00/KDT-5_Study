#1-1
em = 'kim1234@naver.com'
print(em[:7])

#1-2
dom = 'http://www.naver.com'
print(dom[7:])

#1-3
name = "홍길동"
print(name[1:])

#1-4
alp = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRr'
print(alp[::2])
print(alp[1::2])

#1-5
alpnum = 'ABC1DEF2GHI3JKL4MNO5PQR6STU7VWX8YZ'
print(alpnum[3::4])

#1-6
number = "881120-1068234"
print(number[:6])
print(number[7:])

#2
num = int(input("정수 입력 :"))
print(f'10진수 {num}\n16진수 : {hex(num)}\n8진수 : {oct(num)}\n2진수 : {bin(num)}')

#3
a = input("단어 입력 :")
b = input("단어 입력 :")
c = input("단어 입력 :")

print(f'코드 값이 가장 큰 단어 : {max(a, b, c)}\n코드 값이 가장 작은 단어 : {min(a, b, c)}')

#4
message = "오늘은 행복한 목요일입니다."
word = input("단어 입력 :")

print(f'\'{word}\' 단어 메시지 존재 여부 : {word in message}')

#5

word2 = input("단어 입력 :")
# zoo
# 012
# (1) 문자 1개에 대한 코드값 => ord('문자 1개')
# (2) 원하는 진수 변환 => bin(10진수 코드값), hex(10진수 코드값)

print(f'\'{word2}\' 코드값 : {bin(ord(word2[0]))} {bin(ord(word2[1]))[2:]} {bin(ord(word2[2]))[2:]} ')
