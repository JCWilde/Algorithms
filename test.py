from random import choice

words = [w.strip('\n') for w in open('wordlist.txt')]

chosen = [choice(words) for _ in range(10)]

for i in range(len(chosen)):
    print("{}. {}".format(i + 1, chosen[i]))