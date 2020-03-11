def floyd_warshall(M):
    C = M[:]

    for k in range(len(C)):
        for i in range(len(C)):
            for j in range(len(C)):
                if C[i][k] + C[k][j] < C[i][j]:
                    C[i][j] = C[i][k] + C[k][j]

    return C

def create_adjacency_matrix(V, E):
    M = [[float("inf")]*len(V) for v in V]
    for i in range(len(V)):
        M[i][i] = 0
    for weight, u, v in E:
        M[V.index(u)][V.index(v)] = weight
        M[V.index(v)][V.index(u)] = weight
    return M

def pr(M):
    for i in range(len(M)):
        for j in range(len(M[0])):
            print(M[i][j], end=' ')
        print()

V = list('abcde')
E = [(int(e[0]), e[1], e[2]) for e in '1ab 8ae 3be 2bc 4cd 6de'.split(' ')]
M = create_adjacency_matrix(V, E)

pr(M)
print()
pr(floyd_warshall(M))
