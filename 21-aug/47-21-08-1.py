a=int(input())
l=[]
r=0
for i in range(1,6):
    i=i*a
    l.append(i)
print(l)
b=sum(l)
print(b)
if b%2==0:
    print('Even')
else:
    print('odd')
while(b>0):
    m=b%10
    r=(r*10)+m
    b=b//10

print('The reverse of output is',r)
