g=int(input("enter a number"))
a=0
b=g
while b>0:
        d=b%10
        a+=d**3
        b//=10
if g==a:
        print("armstrong number")
else:
        print("not a armstrong number")
        
if g>1:
    for i in range(2,g):
         if(g%i)==0:
             print("prime number")
             break
    else:
        print("not an prime number")
  
