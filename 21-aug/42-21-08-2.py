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

n=int(input())
l=[]
r=0
for i in range(1,6):
    i=i*n
    l.append(i)
print(l)
q=sum(l)
print(q)
if q%2==0:
    print('Even')
else:
    print('odd')


	