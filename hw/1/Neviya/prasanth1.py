a=0
b=0
s=str(input())
s.lower()
for i in s:
    if(i=='a' or i=='e' or i=='o' or i=='i' or i=='u'):
        a=a+1
    else:
        b=b+1
print(a)
print(b)
