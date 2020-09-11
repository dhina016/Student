a=int(input())
n=0
for i in range(1,a):
    if(n%1==0):
        a=a+i
if(a==n):
    print(n,"perfect number")
else:
    print(n,"is not perfect number")
    
