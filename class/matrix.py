# addtion
# m,n = 3,3
# a = [[1,2,8], [1,2,5],[1,2,3]]
# b = [[1,5,3], [1,2,3],[1,2,3]]
# c = []
# for i in range(n):
#     c.append([0 for j in range(m)])
# print(c)
# if m == n:
#     for i in range(m):
#         for j in range(n):
#             c[i][j] = a[i][j] + b[i][j]
#     print(c)
# else:
#     print('not valid matrix')

# # m,n = 3,3
# # a = [[1,2,3], [1,2,3],[1,2,3]]
# # b = [[1,2,3], [1,2,3],[1,2,3]]
# c = []
# for i in range(m):
#     c.append([0 for i in range(n)])
# if m == n:
#     for i in range(m):
#         for j in range(n):
#             c[i][j] = a[i][j] + b[i][j]
#     print(c)
# else:
#     print('not valid matrix')

# m,n = 3,3
# a = []
# for i in range(m):
#     a.append([0 for i in range(n)])
# # a = [[0]*m]*n
# c = [
#     [1,2,3], 
#     [1,2,3],
#     [1,2,3]]
# d = [
#     [1,2,3], 
#     [1,2,3],
#     [1,2,8]
#     ]
# for i in range(m):
#     for j in range(n):
#         for k in range(n):
#             a[i][j] += c[i][k] * d[k][j]
# print(a)

# output = [ 
#     [ 7, 14, 21 ], [0,0,0]
#  ]

# m,n = 2,3
a = [
    [1,2,3],
    [1,2,3]
    ]
# b = []
# for i in range(n):
#     b.append([0 for i in range(m)])
# '''
# [1,1],  
# [2,2],
# [3,3]
# '''
# for i in range(n):
#     for j in range(m):
#         b[i][j] = a[j][i]
# print(b)
l = []
for i in zip([1,2,3], [1,2,3]):
    l.append(list(i))
print(l)