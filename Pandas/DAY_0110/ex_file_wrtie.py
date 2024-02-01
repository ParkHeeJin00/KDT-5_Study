# --------------------------------------------------------------------
# 파일 입출력 => 출력 즉, 쓰기(write)
# - 사용 내장 함수 : open(file, mode = 'w', encoding = '지정')
# --------------------------------------------------------------------
filename = 'mydata.txt'
existfile = 'message.txt'

# (1) open => 쓰기(w) 모드의 경우 파일이 없으면 생성, 있으면 모든 내용 지움
# file = open(filename, mode = 'w', encoding='utf8')

# (1) open => 쓰기(a) 모드의 경우 파일이 없으면 생성, 있으면 제일 마지막에 추가 / append
file = open(filename, mode = 'a', encoding='utf8')

# (2) write
file.write("12345556\n")  ## write에는 줄바꿈 기능 없음 - \n을 입력해야 함
file.write("""ga ga ga    
afdlfdf
121211
""")                      ## 여러줄 적기는 줄바꿈 된 상태로 입력됨

file.writelines(['a','b','111111'])  ## 줄바꿈 기능 없음

# (3) close
file.close()