# fibonnaci
# 0 1 1 2 3 5 8 .....

length = int(input())
a,b =0,1
for i in range(length):
    print(a)   # 0 1 1
    temp = a+b # 1 2 
    a = b      # 1 1
    b = temp   # 1 2
