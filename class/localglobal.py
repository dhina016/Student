recursion   4! = 1*2*3*4

def fact(n):
    if n == 1:
        return n
    else:
        return n*fact(n-1)  # 4*3*2*1

print(fact(5))

global x
x = 1

def l():
    print(x+2) # 3

def k():
    print(x-2) # -1

l()
k()
print(x)

