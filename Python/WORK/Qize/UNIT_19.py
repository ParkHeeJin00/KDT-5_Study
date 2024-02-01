# [연습문제] 19.5
for i in range(5):
    for j in range(5):
        if j<i:
            print(" ", end = '')
        else:
            print("*", end ='')
    print()

#for i in range(5):
#    print(' '* i, '*'*(5-i))

# [심사문제] 19.6

high = int(input())

for i in range(high):
    print(" "*(high-i-1), "*"*(2*i+1))
# high == 5
# " " => 4 3 2 1 0
# "*" => 1 3 5 7 11
# ex) high = 5 i = 0    ==> " " : 4 / "*" : 1
# ex) high = 5 i = 1    ==> " " : 3 / "*" : 3
# ex) high = 5 i = 2    ==> " " : 2 / "*" : 5

