j= int(input())
if j > 1:
    for i in range(2, j):
        if (j % i) == 0:
            print("it is not a prime number")
            break
    else:
        print("it is a prime number")
else:
    print("it is not a prime number")
v=str(j)
n=0
for i in v:
     n=n+int(i) **3
if n==j:
	print("it is an armstrong")
else:
	print("it is not an armstrong"

J=input("String 1:")
N=input("String 2:")
if(sorted(J)==sorted(N)):
      print("The strings are anagrams")
else:
      print("The strings aren't anagrams")