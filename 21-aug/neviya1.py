s=int(input())
total=0
for i in range (5):
	print(s)
	total =total +s
	s=s+2
print (total)
if (total%2==0):
	print('even')
else:
	print('odd')