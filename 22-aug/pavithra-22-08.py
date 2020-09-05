#program 01
a=int(input())
if a>1:
	for i in range(a):
		if(a%i)==0:
		      print(a,"not a prime number")
        else:
        	print(a,"is a prime number")


#program 02
a=int(input())
sum=0
temp=a
while temp>0:
        	b=temp%10
        	sum+=b**3
        	temp//=10
if a==sum:
        	print(a,"is an armstrong number")
else:
        	print(a,"is not a armstrong number")


#program 03 anagram
str1=input()
str2=input()
if(sorted(str1))==(sorted(str2)):
	print("the strings are anagram")
else:
	print("the strings are not anagram")
