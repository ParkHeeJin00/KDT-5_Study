# 24.4
path = 'C:\\users\\dojang\\AppData\\Local\\Programs\\Python\\Python36-32\\python.exe'

filename = path.split("\\")[-1]
print(filename)

# 24.5
strList = list(input().split())

cnt = 0
for i in strList:
    if i in 'the':
        cnt += 1
print(cnt)

# 24.6
priceList = list(map(int,input().split(";")))

priceList.sort(reverse = True)

for i in priceList:
    i = int(i)
    print(f'{i:9,}')