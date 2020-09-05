a = input() # aabcd
b = input() # aacbd
d = set(a) # (a,b,c,d)
for i in d: #a b
    if a.count(i) != b.count(i): #  2 2
        print('Not anagram')
        break
else:
    print('anagram')

a = list(a)
a.sort()
print(a)
