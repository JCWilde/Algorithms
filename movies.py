class Graph(dict):
    def add(self, v):
        self[v] = set()

    def add_edge(self, u, v):
        self[u].add(v)
        self[v].add(u)


class Digraph(dict):
    def add(self, v):
        self[v] = set()

    def add_edge(self, u, v):
        self[u].add(v)


def bfs(Graph, start, goal):
    waiting = [start]
    parent = {start: None}
    while len(waiting) > 0:
        w = waiting.pop(0)

        for x in Graph[w]:
            if x == goal:
                path = [x]
                x = w
                while parent[x] != None:
                    path.append(x)
                    x = parent[x]
                path.append(x)
                path.reverse()
                return path

            if x not in parent:
                parent[x] = w
                waiting.append(x)
    return []


# Returns a list of the components of a graph
def components(G):
    components = []
    found = set()
    for x in G:
        if x not in found:
            C = []
            waiting = [x]
            found.add(x)
            found2 = {x}
            while len(waiting) > 0:
                w = waiting.pop()
                for n in G[w]:
                    if n not in found:
                        waiting.append(n)
                        found.add(n)
                        found2.add(n)
            components.append(found2)
    return components



G = Graph()

lines = [line.strip() for line in open("movies.txt")]
for line in lines:
    pieces = line.split('/')
    for p in pieces:
        if p not in G:
            G.add(p)
    for a in pieces[1:]:
        G.add_edge(pieces[0], a)

'''
while True:
    a1 = input("Input first actor: ")
    a2 = input("Input second actor: ")
    print(bfs(G, a1, a2))
'''

C = components(G)
C.sort(key = len, reverse=True)
print(C)
