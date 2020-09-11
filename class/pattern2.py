'''
        * 
      * * 
    * * * 
  * * * * 
* * * * *
'''
a = int(input())

space = 2 * (a-1)

for i in range(a):
    print(" "*space, end="")
    space -= 2
    for j in range(0,i+1):
        print("*",end=" ")
    print()
space = 2
for i in range(a-1, 0, -1):
    print(" "*space, end="")
    space += 2
    for j in range(0,i):
        print("*",end=" ")
    print()
