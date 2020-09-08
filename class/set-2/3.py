# myname
# 1234

a = input()
b = int(input())

count1 = 0
count2 = 0
for i in a:
    count1 += 1
print(count1)

while b>0:
    count2 += 1
    b //= 10
print(count2)