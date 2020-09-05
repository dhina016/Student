s=int(input("Enter a string"))
z=s
t=len(str(s))
last=0
sum=0
if(s>1):
	for i in range(2,s):
		if(s%i==0):
			print("it is not a prime number")
			break
	else:
		print("it is a prime number")
else:
	print("0 is not a prime")
while(z>0):
	last=z%10
	sum+=(last**t)
	z=z//10
if(s==sum):
	print("it is an armstrong  number")
else:
	print("it is not an armstrong number")



