student = {}
for i in range(int(input())):
    a = input().split()
    student[a[0]] = list(map(float, a[1:]))
print('%.2f' %(sum(student[input()])/3))