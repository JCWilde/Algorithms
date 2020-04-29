# -*- coding: utf-8 -*-
from collectionStuff import Counter

words = set(line.strip() for line in open('wordlist.txt'))

hand = 'zzapjeq'

for word in words:
    if len(Counter(word) - Counter(hand)) == 0:
        print(word, Counter(hand) - Counter(word))