a=int(input())
if a>1:
    for i in range(2,a):
        if(a%i)==0:
            print(a,'is prime')
            break
    else:
        print(a,'is not prime')
else:
    print(a,'is not prime')


a=input()
b=input()
c=len(a)
d=len(b)
if(c==d):
    if(sorted(a)==sorted(b)):
        print("Anagram")
    else:
        print("Not Anagram")
else:
    print("Not  Anagram")
    