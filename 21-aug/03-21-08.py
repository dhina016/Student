j=int(input())
n=0
for i in range(5):
    print(j)
    n=n+j
    j=j+2
print(n)
if (n%2==0):
    print("even")
else:
    print("odd")
s=str(int(n))
print(s[::-1])


n=str(input())
j=n[::-1]
if (n==j):
    print("Palindrome")
else:
    print("Not palindrome")
print(len(n))
l=len(n)
if (l%2==0):
    print("Odd")
else:
    print("Even")

J=input("String 1:")
N=input("String 2:")
if(sorted(J)==sorted(N)):
      print("The strings are anagrams")
else:
      print("The strings aren't anagrams")