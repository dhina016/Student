n=int(input())
l=[]
for i in range(1,6):
    a=n*i
    l.append(a)
    print(a)
print(l)
sum=l[0]+l[1]+l[2]+l[3]+l[4]
print(sum)
if sum%2==0:
    print("Even")
else:
    print("ODD")
rev=0
while(sum>0):
    a=sum%10
    rev=rev*10+a
    sum=sum//10
print(rev)
