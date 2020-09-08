'''Python Program to Check Armstrong Number'''
# 153 (1**3+5**3+3**3 == 153)
a = int(input())
value = 0
# for i in a:
#     value += (int(i)**len(a))
# print(int(a) == value)
b = a
while b>0:
    print(b)
    temp = b%10
    value += (temp**len(str(a)))
    b //= 10

print(a==value)
