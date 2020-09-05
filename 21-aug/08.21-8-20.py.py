g=input()
print(len(g))
rev=g[::-1]
if g==rev:
    print("palindrome")
else:
    print("not is palindrome")
if(len(g)%2==0):
    print("even")
else:
    print("Odd")

