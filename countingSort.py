"""
counting sort is useful for arrays of integers
which are contained in a relatively small range.

O(n)

"""

from random import randint


# assumes that list contains non-negative numbers
def CountingSort(L):
    counts = [0] * (max(L) + 1)
    for x in L:
        counts[x] += 1
    print(counts)
    res = []
    for i in range(len(counts)):
        res += [i] * counts[i]
    return res


L = [randint(0, 20) for i in range(50)]
print(L)
print(CountingSort(L))
