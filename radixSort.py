"""
sorts integers based on units digits

O(n)

takes up less space.

"""

from random import randint


def radix_sort(l):
    """
    assumes that list contains non negative numbers
    """
    steps = len(str(max(l)))
    for d in range(steps):
        q = 10 ** d
        buckets = [[] for i in range(10)]
        for x in l:
            buckets[(x // q) % 10].append(x)
        l = [y for bucket in buckets for y in bucket]
    return l


L = [randint(0, 1000) for i in range(50)]
print(L)
print(radix_sort(L))
