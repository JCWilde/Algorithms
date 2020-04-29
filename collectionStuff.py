# -*- coding: utf-8 -*-
from random import randint, choice


L = [5,3,2,9,8,14,5,2,1]

# Quick way
print(max(L))

# long way
biggest = L[0]
for x in L:
    if x > biggest:
        biggest = x
print(biggest)


# find index and value
Biggest = [0,L[0]]
for i in range(len(L)):
    if L[i] > Biggest[1]:
        Biggest = [i,L[i]]
print(Biggest)

# finding the most common item in a list
L = [randint(1,10) for i in range(50)]

#O(n)
def mode(l = list):
    buckets = {}
    for x in l:
        if x not in buckets:
            buckets[x] = 1
        else:
            buckets[x] += 1
    save_key = 0
    biggest = 0
    for key in buckets:
        if buckets[key] > biggest:
            biggest = buckets[key]
            save_key = key
    return save_key, biggest

#O(n^2)
def mode2(l = list):
    biggest = 0
    save_x = 0
    for x in l:
        count = 0
        for y in l:
            if x == y:
                count += 1
        if count > biggest:
            biggest = count
            save_x = x
    return save_x

# O(n)
def mode3(LIST = list):
    l = sorted(LIST)
    print(l)
    save_item = 0
    biggest = 0
    count = 0
    for i in range(len(l) - 1):
        if l[i] == l[i + 1]:
            count += 1
        else:
            if count > biggest:
                biggest = count
                save_item = l[i]
            count = 1
    return save_item

print(mode3(L))


