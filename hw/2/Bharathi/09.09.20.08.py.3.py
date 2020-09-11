a=int(input("enter the number of rows"))
b=65
for i in range(0,a):
    for j in range(0,i+1):
        c=chr(b)
        print(c,end='')
        b+=1
        print()
