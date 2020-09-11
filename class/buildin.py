def oddeven(n):
    if n%2== 0:
        return True
    else:
        return False

def length(s):
    return len(s)


# build-in functions
k = ['qwe', 'qw', 'qwerty', 'qazxsdfg', 'qscx']
# print(abs(-1))
# print(all([True,True,1,'dsa']),any([0,False,True]))
# print(bin(100))
# print(callable())
# print(chr(97))
# print(ord('A'))
# print(complex(3,1))
# print(divmod(5,2))
# print(enumerate([1,2,3,4,5]))
# for i,j in enumerate(l):
#     print(i,j)
# eval('print("hai")')
# l = list(map(int, [1.12, 2.22, 3.33, 44.4, 55.5]))
# print(l)
l = list(filter(oddeven, [1,2,3,4,5]))
print(l)
# print('{}'.format('hai'))
# print(hex(5),oct(5))
# print(isinstance(1.5, float))
# print(min(k), max(k))
# print(pow(2, 3))
# print(list(range(1,8)))
# print(list(reversed('qwerty')))
# print(round(4.112233, 2))
# print(k[slice(1,5,2)])
# print(sorted(k, key=length, reverse=True))
# print(type(k))
# print(list(zip([1,2,3], [2,3,4])))
'''string'''
# s = 'hello wOrldhello world'
# print(s.title())
# print(s.capitalize())
# print(s.lower())
# print(s.casefold())
# print(s.upper())
# print(s.swapcase())
# print(s.isalnum())
# print(s.isalpha())
# print(s.isdigit())
# print(s.count('l'))
# print(s.replace('l', 'k', 1))
# print(s.startswith('hello'))
# print(s.endswith('ld'))
# print(s.rfind('l'))
# print(s.lstrip())
# print(s.index('l'))
# print(s.split(' ', 2))
# print(s.splitlines())
# print(s.partition('wOrld'))
# print('1'.zfill(3))
'''list'''
'''copy, append, clear, index, pop, remove, reverse, sort, count'''

'''Dictionary'''
'''clear, copy, get, keys, pop, popitems,values'''
# d = { 'KEY1': 1, 'KEY2': 2, 'Key3':3 }
# print(d.popitem())
# print(d)
'''set'''
'''add, clear, copy, difference, discard, pop, remove, union, ,intersection, update, subset'''
# s = { 1, 2, 3, 4, 5 }
# s1 = { 1, 2, 3, 9 }
# # s.add(4)
# # s.clear()
# print(s1.issubset(s))
# print(s)

# a = iter([1,2,3])
# print(a.__next__())
# print(next(a))
# print(next(a))
# print(next(a))
