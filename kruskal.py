from heapq import heappop, heappush

class WeightedGraph(dict):
    def __init__(self):
        self.weight = {}
        
    def add(self, v):
        self[v] = set()

    def add_edge(self, weight, u, v):
        self[u].add(v)
        self[v].add(u)
        self.weight[(u,v)] = weight
        self.weight[(v,u)] = weight

def kruskal(G):
    edges = []
    for v in G:
        for w in G[v]:
            if (G.weight[(v,w)], w, v) not in edges:
                edges.append((G.weight[(v,w)],v,w))
    edges.sort()

    P = {v:v for v in G}
    R = {v:0 for v in G}

    mst = []
    while len(mst) < len(G) - 1:
        if len(edges) == 0:
            return []  # no MST. Graph is disconnected
        _, v, w = edges.pop(0)
        if find(P, v) != find(P, w):
            mst.append((v, w))
            union(P, R, v, w)

        # uncomment this code to print out the values of P and R like we did on the board in class
        for v in V:
            print(v, end=' ')
        print()
        for v in V:
            print(P[v], end=' ')
        print()
        for v in V:
            print(R[v], end=' ')
        print('\n')

    return mst


def find(P, v):
    while v != P[v]:
        v = P[v]
    return v

def union(P, R, v, w):
    pv = find(P, v)
    pw = find(P, w)

    if pv != pw:
        if R[pv] < R[pw]:
            P[pv] = pw
        else:
            P[pw] = pv

        if R[pv] == R[pw]:
            R[pv] += 1


    
V = 'abcdefgh'
E = '1ae 1bf 1cg 1dh 2ab 6bc 4cd 3ef 7fg 5gh'

G = WeightedGraph()
for v in V:
    G.add(v)

for e in E.split():
    G.add_edge(int(e[0]), e[1], e[2])

for u,v in kruskal(G):
    print(u, v, G.weight[(u,v)])
