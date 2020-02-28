from collections import defaultdict

class Digraph(dict):
    def add(self, v):
        self[v] = set()

    def add_edge(self, u, v):
        self[u].add(v)

def topo_sort(D):
    order = []

    # For each vertex, build up a count of how many edges point into it
    d = defaultdict(int)
    for x in D:
        for v in D[x]:
            d[v] += 1    
    queue = [x for x in D if d[x]==0]

    while len(queue) > 0 :
        x = queue.pop(0)
        order.append(x)

        # update the indegrees of x's neighbors; add new indegree 0s to queue
        for v in D[x]:
            d[v] -= 1
            if d[v] == 0:
                queue.append(v)

    if len(order) < len(D):   # if this happens, there's a cycle in the digraph
        return []
    else:
        return order


# Testing code
D = Digraph()
for v in "abcdefghij":
    D.add(v)
for e in "ab bc cd ed fe hg ha ie ic ij jb".split():
    D.add_edge(e[0], e[1])
print(topo_sort(D))


for v in "abcde":
    D.add(v)
for e in "ab bc cd da ea".split():
    D.add_edge(e[0], e[1])
print(topo_sort(D))
    
