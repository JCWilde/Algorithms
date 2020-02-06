from random import *
from heapq import *


def heapsort(L):
    H = []
    for x in L:
        heappush(H, x)
    for i in range(len(L)):
        L[i] = heappop(H)


# alternate version, a little faster.  The heapify function turns a list into
# a heap faster than manually pushing the elements.
def heapsort(L):
    H = L[:]
    heapify(H)
    for i in range(len(L)):
        L[i] = heappop(H)


# testing code
L = [4, 6, 14, 9, 7, 2, 11, 5]
print(L)
heapsort(L)
print(L)

L = [randint(1,100) for i in range(100)]
M = L[:]
heapsort(L)
print(L == sorted(M))
