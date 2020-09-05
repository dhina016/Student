s=input()
print(len(s))
rev=s[::-1]
if s==rev:
    print("palindrome")
else:
    print("not is palindrome")
if(len(s)%2==0):
    print("even")
else:
    print("odd")

