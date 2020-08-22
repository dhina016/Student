number=int(input())
l=[]
for i in range(5):
    i+=1
    n=i*2
    l.append(n)
#1
print(*l,sep=' ')
s=sum(l)
#2
print(s)
#3
if s%2==0:
    print(s,'is a Even')
else:
    print(s,'is a Odd')
#4
r=str(s)
r1=r[::-1]
r=int(r1)
print(r)

