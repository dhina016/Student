n=int(input())
#prime number or not
for i in range(2,n):
    if (n%i)==0:
        print(n,'is not a prime number')
        break
else:
    print(n,'is a prime number')

#armstrong or  not
s=str(n)
strl=(len(s))
l=list(s)
r = list(map(int, l))
for i in range(len(r)):
    r[i]=r[i]**strl
a=sum(r)
if a==n:
    print(n,'is a armstrong number')
else:
    print(n,'is not a armstrong number')
