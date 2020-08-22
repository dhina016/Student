l='qwerty'
if l==l[::-1]:
	print('palindrome')
else:
	print('not a palindrome')
print(len(l))
if len(l)%2==0:
	print('even')
else:
	print('odd')