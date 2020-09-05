a=input("enter a string")
b=input("enter a string")
sum=0
dup1=set(a)
dup2=set(b)
t=len(dup1)
x=len(dup2)
for i in dup1:
	if(a.count(i)==b.count(i)):
		sum+=1
	else:
		print("It is not an anagram")
if(t==sum):
	print("it is anagram")