s=input()
b=[]
for i in range(5):
    i+=1
    s=i*2
    b.append(s)
print(*b,sep='')
r=sum(b)
print(r)
c=str(r)
a=c[::-1]
print(a)
if r%2==0:
    print("even")
else:
    print("odd")

    
