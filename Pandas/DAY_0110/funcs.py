def add(x,y): return x+y
def div(x,y): return x/y if y else None

if __name__ == "__main__":   # 파일에서 name이 main이면 실행해라   / main이라는 것은 현재 파일인가 아닌가

    print(f'funcs.py => __name__ : {__name__}')
    print(f'add(3,4) : {add(3,4)}')
    print(f'div(3,4) : {div(3,4)}')