from random import randint

def quicksort(l):
    print(len(l))
    if len(l) < 2:
        return []
    low = []
    for i in l:
        if i <= l[0]:
            low.append(i)
    high = []
    for i in l:
        if i > l[0]:
            high.append(i)
    return quicksort(low) + l[0] + quicksort(high)

L = [randint(0,10) for i in range(100)]
print(L)
L = quicksort(L)
print(L)

