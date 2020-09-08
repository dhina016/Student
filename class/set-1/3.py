'''Python Program to Find the Factorial of a Number'''
# 5*4*3*2*1   1*2*3*4*5

fact = int(input())
d = 1
if(fact == 1):
    print(fact)
else:
    for i in range(fact, 0, -1):
        print(i)
        fact = fact*i
    print(fact)