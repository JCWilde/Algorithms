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

def dijkstra(G, start, goal):
    info = {start: (0, None)}
    heap = [(0, start)]

    while len(heap) > 0:
        _, w = heappop(heap)

        if w == goal:
            P = [w]
            while info[w][1] != None:
                w = info[w][1]
                P.append(w)
            P.reverse()
            return P

        cost = info[w][0]
        for n in G[w]:
            weight = G.weight[(w,n)]
            if n not in info or cost + weight < info[n][0]:
                info[n] = (cost + weight, w)
                heappush(heap, (cost + weight, n))
    return []
    
    
V = 'abcdefg'
E = '1ab 1be 5eg 1gf 8fc 9ca 4ad 2bd 4ed 2fd 5cd 9gd'

G = WeightedGraph()
for v in V:
    G.add(v)

for e in E.split():
    G.add_edge(int(e[0]), e[1], e[2])

print(dijkstra(G, 'a', 'g'))
