n=int(input())
       a=0
       h=1
      while h<=n/2:
	if n%h==0:
	   a=1
	break
           h=h+1
		
if a==0:
	print('the given number is prime num',n)
else:
	print('the given number is not a prime number',n)

num = int(input("enter a number"))  
sum=0  
temp=num  
while temp>0:  
    digit=temp%10  
    sum+= digit**3  
    temp //= 10  
if num == sum:  
    print(num,"is an armstrong number")  
else:  
    print(num,"is not an armstrong number")

a=input('first string')
a1=input ('second string')
if(sorted(a)==sorted(a1)):
   Print('the sorted strings are anagrams')
else:
    Print('the sorted strings are not anagrams')
   
