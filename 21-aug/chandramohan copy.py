s=input()
if ( s==s[::-1]):
	if ( s%2==0):
		print('s is add')
	print('is palindrome')
else:
	print ( ' not a palindrome ')

	print(len(s))
	print('s is even')


a=int(input())
s=0
for i in range(1,6):
	n=a*i
	print('the number is',n)
	s=s+n
print('the sum of number is ',s)
if (s%2==0):
	print('s is even')
n=s//10
print(n)
