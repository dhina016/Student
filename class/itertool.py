from itertools import permutations, combinations, combinations_with_replacement, product, compress, starmap

# perm = list(permutations('AGA', 2))
# print(len(perm), perm)

l = [1, 2, 3, 4, 5]
# combo = list(combinations(l, 6))
# combo2 = list(combinations_with_replacement(l, 3))
# print(len(combo), combo)
# print(len(combo2), combo2)
# print(list(product([1, 2, 3, 4], [2, 3])))
combo = list(combinations(l, 3))
print(combo)
print(list(starmap(min, combo)))
