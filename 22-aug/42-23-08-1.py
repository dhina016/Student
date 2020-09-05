a=int(input())
d=len(str(a))
b=0
t=a
while(t>0):
    c=t%10
    b+=c**d
    t//=10
if a==b:
    print(a,'is armstrong')
else:
    print(a,'is armstrong')