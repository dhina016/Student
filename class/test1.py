# get num from user
# call factorial method and return to main hint: 4!  = 1*2*3*4 
# check odd even of returned factorial number : method name oddEven
# if even sum of digit  : method name digit()
# else print not valid 

def fact(n):
    b = 1
    while(n>0):
        b = b*n
        n = n-1
    return b

def oddEven(i):
    if i%2 == 0:
        return 'even'
    else:
        return 'odd'

def digit():
    pass


num = int(input())
val = fact(num)
print(val)
