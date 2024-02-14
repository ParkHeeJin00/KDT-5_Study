# filename1 = input("원본 파일 이름을 입력하시오: ")
# filename2 = input("복사 파일 이름을 입력하시오: ")
# infile = open(filename1, "rb")
# outfile = open(filename2, "wb")
# # 입력 파일에서 1024 바이트씩 읽어서 출력 파일에 쓴다.
# # 파일의 마지막 부분에서는 읽어 들인 바이트 수만큼 파일에 저장
# while True:
#     copy_buffer = infile.read(1024)
#     print(len(copy_buffer)) # 실제 읽어온 바이트 수 출력
#     if not copy_buffer: # 파일의 끝인 경우, empty byte를 리턴
#         break
#
# outfile.write(copy_buffer)
# infile.close()
# outfile.close()
# print(filename1+"를 " + filename2 +"로 복사하였습니다. ")


# 예외처리 #1
(x,y) = (2,0)
try:
    z = x/y
except ZeroDivisionError:
    print ("0으로 나누는 예외")

(x,y) = (2,0)
try:
    z = x/y
except ZeroDivisionError as e:  # e : 파이썬이 제공하는 에러 메시지
    print(e)

while True:
    try:
        n = input("숫자를 입력하시오 : ")
        n = int(n)
        break
    except ValueError:
        print("정수가 아닙니다. 다시 입력하시오. ")
print("정수 입력이 성공하였습니다!")

def calc(values):
    sum = None
    try:
        sum = values[0] + values[1] + values[2]
    except IndexError as err:
        print("인덱스 에러: " , err)
    except Exception as err:
        print(err)
    else:
        print("에러 없음:", values)
    finally:
        print(f"sum={sum}")

calc([1, 2, 3])
calc([1, 2])

# 파일 안의 각 문자 횟수 세기
filename = input("파일명을 입력하세요: ").strip()
infile = open(filename, "r")
freqs = {} # 딕셔너리 생성
# 파일의 각 줄에서 문자를 추출한 다음 각 문자를 dict에 추가
for line in infile:
    for char in line.strip():
        if char in freqs:
            freqs[char] += 1 # 딕셔너리에 key(char)가 있으면 증가
    else:
        freqs[char] = 1 # 딕셔너리에 key(char)가 없으면 추가
print(freqs)
infile.close()