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

def prim(G, start):
    found = set(start)
    mst = []
    heap = []
    
    # add all edges out of start into the heap
    for v in G[start]:
        heappush(heap, (G.weight[(start, v)], start, v))
    
    while len(heap) > 0 and len(mst) < len(G) - 1:
        if len(heap) == 0:
            return []   # graph not connected, no mst

        _, u, v = heappop(heap)
        if v not in found:
            mst.append((u,v))
            found.add(v)
            for w in G[v]:
                heappush(heap, (G.weight[(v,w)], v, w))

    return mst

V = 'abcdefghij'
E = '1ab 4bc 2cd 7de 3ef 4fg 1gh 1ag 5ai 3ig 6ij 3bj 1fj 2jd 2ah'

G = WeightedGraph()
for v in V:
    G.add(v)

for e in E.split():
    G.add_edge(e[0], e[1], e[2])

#print(G.weight[('a', 'b')])
for u,v in prim(G, 'a'):
    print(u, v, G.weight[(u,v)])
