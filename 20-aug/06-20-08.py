a="abcdef"
b=a.replace('a','b')
print(b)

a='aaaaaa'
b=a.replace('a','b')
print(b)

a=123456
b=list(map(int,str(a)))
print(b)
print(b[::-2])
print(b[-2::-2])