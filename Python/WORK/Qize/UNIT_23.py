# 23.6
a = [[[0 for col in range(3)]for row in range(4)]for height in range(2)]

print(a)

# 23.7
col, row = map(int, input().split())

emList = []
for i in range(col):
    emList.append(list(input()))

for i in range(col):
    for j in range(row):
        if emList[i][j] == '*':
            print('*', end ='')
        else:
            cnt = 0
            for i2 in list(n for n in range(i-1,i+2) if (0<=n<=col-1)):
                for j2 in list(n for n in range(j-1,j+2) if (0<=n<=row-1)):
                    if emList[i2][j2] == "*":
                        cnt += 1
                    else:
                        pass
            print(cnt, end ='')
    print()



