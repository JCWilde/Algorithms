# -*- coding: utf-8 -*-
from random import randint, shuffle


def slow_sort(L):
    '''
    O(n^2)
    O(1) in memory usage
    '''
    for i in range(len(L)):
        for j in range(i + 1, len(L)):
            if L[j] < L[i]:
                L[i], L[j] = L[j], L[i]

def bogosort(L):
    '''
    O(n!)
    '''
    while True:
        shuffle(L)
        print(''.join(str(l) for item in L))
        for i in range(len(L)-1):
            if L[i + 1] < L[i]:
                break
        else:
            return

l = [randint(0,100) for i in range(10)]

slow_sort(l)

print(l)

l = [randint(0,1) for i in range(20)]

bogosort(l)

print(l)