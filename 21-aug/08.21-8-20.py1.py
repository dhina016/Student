g=input()
a=[]
for i in range(5):
    i+=1
    g=i*2
    a.append(g)
print(*a,sep='')
s=sum(a)
print(s)
f=str(s)
k=f[::-1]
print(k)
if s%2==0:
    print("even")
else:
    print("odd")

    
