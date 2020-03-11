
class WeightedGraph(dict):
    def __init__(self):
        self.weight = {}

    def add(self, v):
        self[v] = set()

    def add_edge(self, weight, u, v):
        self[u].add(v)
        self[v].add(u)
        self.weight[(u, v)] = weight
        self.weight[(v, u)] = weight


def path(parent, v):
    P = [v]
    while parent[v] is not None:
        v = parent[v]
        P.append(v)
    P.reverse()
    return P


def bellman_ford(G, start):
    parent = {start: None}
    d = {v:float('inf') for v in G}
    d[start] = 0

    for i in range(len(G) - 1):
        for u in G:
            for v in G[u]:
                weight = G.weight[(u, v)]
                if d[u] + weight < d[v]:
                    d[v] = d[u] + weight
                    parent[v] = u
    return d, {v:path(parent, v) for v in G}


def bellman_ford_disp(G, start):
    parent = {start: None}
    d = {v:float('inf') for v in G}
    d[start] = 0

    for i in range(len(G) - 1):
        for u in G:
            for v in G[u]:
                weight = G.weight[(u, v)]
                if d[u] + weight < d[v]:
                    d[v] = d[u] + weight
                    parent[v] = u
            print(u, end=' ')
            for v in d:
                print(' I' if d[v] == float("inf") else "{:2d}".format(d[v]), end = ' ')
            print()
        print('-' * 40)

V = 'abcdefg'
E = '12,a,b 4,a,d 1,a,c 20,b,c 5,c,e 2,b,e 2,b,f 2,e,g 1,g,f'

G = WeightedGraph()
for v in V:
    G.add(v)

for e in E.split(' '):
    vals = e.split(',')
    G.add_edge(int(vals[0]), vals[1], vals[2])

bellman_ford_disp(G, 'g')
d, p = bellman_ford(G, 'g')
for v in G:
    print(d[v], p[v])