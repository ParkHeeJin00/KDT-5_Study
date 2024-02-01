# 18.5
i = 0
while True:
    if i>73:break
    if i % 10 != 3:
        i += 1
        continue
    print(i, end=" ")
    i += 1


print()

# 18.6
start, stop = map(int, input().split())
i = start

while True:
    if i > stop:break

    if 1<=start<=200 and 10<=stop<=200 and start<stop:
        if i % 10 != 3:
            print(i, end=" ")
        i += 1

