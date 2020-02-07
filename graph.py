class Graph(dict):
    def add(self, v):
        self[v] = set()

    def add_edge(self, u, v):
        self[v].add(u)
        self[u].add(v)


class Digraph(dict):
    def add(self, v):
        self[v] = set()

    def add_edge(self, u, v):
        self[v].add(u)

V = "abcde"
E = "ab ac bc ad ad"

G = Graph()
for v in V:
    G.add(v)
for e in E.split(' '):
    G.add_edge(e[0], e[1])

print("Neighbors for a: {}".format(G['a']))

print("Is there a vertex z? {}".format('z' in G))

print("Is there an edge from a to b? {}".format('b' in G['a']))

print("Number of vertices: {}".format(len(G)))

numEdge = 0
for v in G:
    numEdge += len(G[v])
numEdge = numEdge // 2

print("Number of edges: {}".format(numEdge))

print(G)