#1
num1 = int(input("숫자를 입력하세요."))
num2 = int(input("숫자를 입력하세요."))
print(f'{num1} + {num2} = {num1+num2}')
print(f'{num1} - {num2} = {num1-num2}')
print(f'{num1} * {num2} = {num1*num2}')
print(f'{num1} / {num2} = {num1/num2}')
print(f'{num1} // {num2} = {num1//num2}')
print(f'{num1} % {num2} = {num1%num2}')
print(f'{num1} ** {num2} = {num1**num2}')

#2
print(f'{num1}>{num2}\t=> {num1>num2}')
print(f'{num1}<{num2}\t=> {num1<num2}')
print(f'{num1}<={num2}\t=> {num1<=num2}')
print(f'{num1}>={num2}\t=> {num1>=num2}')
print(f'{num1}=={num2}\t=> {num1==num2}')
print(f'{num1}!={num2}\t=> {num1!=num2}')

#3
num_max = int(input("최대값을 입력하세요."))
num_min = int(input("최소값을 입력하세요."))
print(f'{num1}=={num2} and {num1}>{num_max}\t=> {num1==num2 and num1>num_max}')
print(f'{num1}=={num2} and {num1}>{num_min}\t=> {num1==num2 and num1>num_min}')
print(f'{num1}=={num2} or {num1}>{num_max}\t=> {num1==num2 or num1>num_max}')
print(f'{num1}=={num2} or {num1}>{num_min}\t=> {num1==num2 or num1>num_min}')
print(f'not {num1}\t=> {not num1}')
