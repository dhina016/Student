a=input()
if(a==a[::-1]):
    print(a,'is a palindrome')
else:
    print(a,'is not a palindrome')
b=len(a)
print(b)
if b%2==0:
    print('even')
else:
    print('odd')
