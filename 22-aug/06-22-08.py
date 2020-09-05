a=int(input())
b=str(a)
c=len(b)
e=0
if(a>1):
	for i in range(2,a-1):
		if( a%i==0 ):
			print("It is not a prime number")
			break
	else:
		print("It is  a prime number ")
else:
	print("It is nethier prime nor composite")
for i in b:
	d=a%2
	e=e+d**c
	a=a//2
if (e==b):
	print("It is an armstrong number")
else:
	print("It is not a armstrong number")


a=int(input())
b=str(a)
c=len(b)
e=0
if(a>1):
	for i in range(2,a-1):
		if( a%i==0 ):
			print("It is not a prime number")
			break
	else:
		print("It is  a prime number ")
else:
	print("It is nethier prime nor composite")
for i in b:
	e=e+int(i)**c
if (e==a):
	print("It is an armstrong number")
else:
	print("It is not a armstrong number")


a,b=map(str,input().split())
c=sorted(a)
d=sorted(b)
if (c==d):
	print("It is an anagram")
else:
	print("It is not a anagram")