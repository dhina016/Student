n=int(input())
l=[]
for i in range(1,6):
    i=i*n
    l.append(i)
print(l)
q=sum(l)
print(q)
if q%2==0:
    print('Even')
else:
    print('odd')


	