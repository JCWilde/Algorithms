from heapq import heappop, heappush


class WeightedGraph(dict):
    def __init__(self):
        self.weight = {}

    def add(self, v):
        self[v] = set()

    def add_edge(self, weight, u, v):
        self[v].add(u)
        self[u].add(v)
        self.weight[(u, v)] = weight
        self.weight[(v, u)] = weight


def prim(G, start):
    found = set(start)
    mst = []
    heap = []
    for v in G[start]:
        heappush(heap, (G.weight[(start, v)], start, v))
    while len(heap) > 0 and len(mst) < len(G) - 1:
        if len(heap) == 0:
            return []
        _, u, v = heappop(heap)
        if v not in found:
            mst.append((u, v))
            found.add(v)
            for w in G[v]:
                heappush(heap, (G.weight[(v, w)], v, w))
    return mst


V = 'a b c d e f g h i j'
E = '1,a,b 2,a,h 5,a,i 1,h,g 4,g,f 3,f,e 7,e,d 1,f,j 3,g,i 6,i,j 3,b,j 4,b,c 2,c,d 2,j,d'

G = WeightedGraph()
for v in V.split():
    G.add(v)

for e in E.split():
    e = e.split(',')
    G.add_edge(e[0], e[1], e[2])


L = prim(G, 'a')
for x, y in L:
    print("{} {} {}".format(x, y, G.weight[(x, y)]))