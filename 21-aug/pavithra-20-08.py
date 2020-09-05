#program 01 multiple of 2 
a=int(input())
l=[]
m=0
for i in range(1,6):
	i=i*a
	l.append(i)
print(l)
s=sum(l)
print(s)
if s%2==0:
	print("the given number is even")
else:
	print("the given number is odd")
x=int(m%10)
y=int(m/10)
print(x,y)





#program 02 palindrome or not
str=(input())
if(str==str[::-1]):
	print("the string is palindrome")
else:
	print("the string is not palindrome")