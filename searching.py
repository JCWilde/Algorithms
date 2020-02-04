# -*- coding: utf-8 -*-

def search(L, x):
    '''
    O(n)
    '''
    for y in L:
        if y == x:
            return True
    return False
    
# needs to be sorted O(log n)
def binary_search(L, x):
    l = sorted(L)
    lo = 0
    hi = len(l) - 1
    while hi != lo:
        mid = (hi + lo) // 2
        if x == l[mid]:
            return True
        elif x > l[mid]:
            lo = mid + 1
        else:
            hi = mid - 1
    return False
            
        





for i in range(10):
    print(i,binary_search([1,2,3,4,5,6,7],i))