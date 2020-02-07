def riffle(L):
    final = []
    for i in range(len(L)//2):
        final.append(L[i])
        final.append(L[len(L)//2 + i])
    return final


L = list(range(1, 53))

for i in range(8):
    L = riffle(L)
    print(L)
    print(L)
