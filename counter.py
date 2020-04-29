# -*- coding: utf-8 -*-

from collectionStuff import Counter

from random import choice

s = 'mikemikemichealjavon'
print(Counter(s))

print()

def mode(L):
    d = Counter(L)
    items = list(d.items())
    return sorted(items, key = lambda x : x[1], reverse = True)[0][0]

l = [choice('abcdefghijkmnopq') for i in range(100)]
print(Counter(l))
print(mode(l))

