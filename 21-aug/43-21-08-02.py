string=input()
#1
r=string[::-1]
if string==r:
    print(string,'is a palindrome')
else:
    print(string,'is a not palindrome')
#2
l=len(string)
print(l)
#3
if l%2==0:
    print(l,'is a Even')
else:
    print(l,'is a odd')
