n=int(input("enter a num")) 
m=0
Rev=0
for i in range(1, 6) :
           s=n*i
           print(s, end=' ') 
           m=m+s
print("\n sum is", m) 
a="even" if m%2 else "odd"
print(a) 
b=str(m) 
print("reverse", b[::-1])

c=input("enter a string") 
t="palindrome"if c==c[::-1] else"not palindrome"
y=len(c) 
z="even" if y%2==0 else "odd"
print(t)
print(z)