# ------------------------------------------------------------
# 파일 데이터 접근 관련 메서드
# ------------------------------------------------------------
filename = 'message.txt'

with open(filename, mode = 'r', encoding='utf8') as f:
    f.seek(5)
    print(f.read(10))   ## 5 위치에서부터 10 byte 읽기
    print(f'현재 위치 : {f.tell()}')
    f.seek(0)
    print(f.read(5))
    print(f'현재 위치 : {f.tell()}')


print(f.name, f.closed)
