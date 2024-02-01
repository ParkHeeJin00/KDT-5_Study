# [연습문제] 29.7
x = 10
y = 3
def get_quotient_remainder(a,b):
    return a//b, a%b

quotient, remainder = get_quotient_remainder(x,y)
print(f'몫 : {quotient}, 나머지 : {remainder}')

# [심사문제] 29.8
x, y = map(int,input().split())
def calc(a,b):
    return a+b, a-b, a*b, a/b
a,s,m,d = calc(x,y)
print(f'덧셈: {a}, 뺄셈: {s}, 곱셈: {m}, 나눗셈: {d}')