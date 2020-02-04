# -*- coding: utf-8 -*-

l = [1,2,5,3,2,9,10]

print(sorted(l))


l = [1,2,5,3,2,9,10]

l.sort()
print(l)

l = [1,2,5,3,2,9,10]

l.sort(reverse = True)
print(l)

words = [line.strip() for line in open('wordlist.txt')]
words.sort(key=len)
print(words[:50])
print(words[-50:])

l = [(4,5),(7,10),(5,3),(14,2),(6,1)]
l.sort()
print(l)

l = [(4,5),(7,10),(5,3),(14,2),(6,1)]
l.sort(key = lambda x : x[1])
print(l)

l = [(4,5),(7,10),(5,3),(14,2),(6,1)]
l.sort(key = lambda x : x[0] + x[1])
print(l)