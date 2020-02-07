from random import *

def shuffle(L):
    """

    Mike's Algorithm
    O(n^2)

    """
    nl = []
    copy = L[:]

    for i in range(len(L)):
        rand_index = randint(0, len(copy) - 1)
        nl.append(copy[rand_index])
        del copy[rand_index]
    return nl


def shuffle2(L):
    """

    O(n)

    """
    for i in range(len(L) - 1):
        rand_index = randint(i + 1, len(L) - 1)
        L[i], L[rand_index] = L[rand_index], L[i]
    return L

l = list(range(10))

print(shuffle2(l))

