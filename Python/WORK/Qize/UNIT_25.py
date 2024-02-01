# [연습문제] 25.7
maria = {'korean': 94, 'english':91,'mathematics':89,'science':83}
average = sum(maria.values())/len(maria)
print(average)

# [심사문제] 25.8
keys = input().split()
values = map(int,input().split())

x = dict(zip(keys,values))

x = {keys:values for keys, values in x.items() if keys != 'delta' and values != 30}

print(x)
