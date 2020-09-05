n=int (input())
a=0
for i in range(1,6):
	b=i*n
	print(b,end=' ')
	a=a+b
print('\n',a)
if a%2==0:
	print('even')
else:
	print('odd')
c=int(a%10)
d=int(a/10)
print(c,d,end=" ")


a=input()
b=a[::-1]
if a==b:
	print(' palindrome')
else:
	print('not palindrome')
print(len(a))
if len (a)%2==0:
	print('even')
else:
	print('odd')