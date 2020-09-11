''' 1.Perfect Number'''
a=int(input())
n=0
for i in range(1,a):
    if(n%1==0):
        a=a+i
if(a==n):
    print(n,"Is a Perfect Number")
else:
    print(n,"It is Not a perfect number")

'''2.Count Vowels in a given string'''
a=0
b=0
s=str(input())
s.lower()
if i in s:
    if(i=='a' or i=='e' or i=='o' or i=='i' or i=='u'):
        a=a+1
    else:
        c=c+1
print(a)
print(b)
