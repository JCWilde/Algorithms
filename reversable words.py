words = set(w.strip('\n') for w in open('reversable words/wordlist.txt'))

for w in words:
    if w[::-1] in words:
        print('{} -> {}'.format(w,w[::-1]))