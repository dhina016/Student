'''
*
**
***
'''
# 1st pattern
a = int(input())
for i in range(1, a+1):
    print('*'*i)
for i in range(a-1, 0, -1):
    print('*'*i)

'''
***
**
*
'''

# 2nd pattern

# for i in range(a,0,-1):
#     for j in range(i-1, 0, -1):
#         print('*', end='')
#     print()