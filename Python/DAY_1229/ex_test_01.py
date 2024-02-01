#1

word = input("단어 입력 :")
print(f'{word} 알파벳 구성 여부 : {word.isalpha()}')
print(f'{word} 숫자 구성 여부 : {word.isnumeric()}')
print(f'{word} 알파벳  대문자로만 구성 여부 : {word.isupper()}')
print(f'{word} 알파벳 소문자로만 구성 여부 : {word.islower()}')


#2

file = input("파일명 입력 :")
print(f'{file} text 파일 여부 : {file.endswith("txt")}')
print(f'{file} jpg 파일 여부 : {file.endswith("jpg")}')
print(f'{file} py 파일 여부 : {file.endswith("py")}')

