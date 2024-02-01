# [연습문제] 22.9
a = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'hotel','india']
b = [i for i in a if len(i) ==5]

print(b)

# [심사문제] 22.10
x, y =map(int, input().split())

listx_y = []
if 1<=x<=20 and 10<=y<=30 and x<y:
    for i in range(x, y+1):
        listx_y.append(2**i)
del listx_y[1]
del listx_y[-2]
print(listx_y)
