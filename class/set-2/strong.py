def fact(n):
    if(n == 1):
        return n
    else:
        return n*fact(n-1)

a = int(input())
c = a
s = 0
while(a>0):
    b = a%10
    s += fact(b)
    a //= 10
if(s == c):
    print('strong')
else:
    print('no')