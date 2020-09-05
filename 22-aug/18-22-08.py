a=int(input())
v=str(a)
b=list(v)
c=len(b)
e=0
for i in range(c):
	d=pow(int(b[i]),c)
	e=e+d
	if(a==e):
		print("armstrong number")
	else:
		print("not an armstrong number")


a=int(input())
if(a%2==0 and a%5==0): # 21
	print('not a prime number')
else:
	print('prime number')

a=input()
b=input()
c,d=len(a),len(b)
if(c==d):
	if (sorted(a)==sorted(b)):
		print("anagram")
	else:
		print("not an anagram")
else:
	print("not an anagram")