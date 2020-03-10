
class Digraph(dict):
    def add(self, v):
        self[v] = set()

    def add_edge(self, u, v):
        self[v].add(u)


def topo_sort(D):
    order = []
    d = {i: 0 for i in range(1000)}
    for x in D:
        for v in D[x]:
            d[v] += 1
    queue = [x for x in D if d[x] is 0]
    while len(queue) > 0:
        x = queue.pop(0)
        order.append(x)
        for v in D[x]:
            d[v] -= 1
            if d[v] is 0:
                queue.append(v)
    return order[::-1]


toClass = {
    120: "CMPSCI I",
    125: "CMPSCI II",
    228: "Discrete",
    247: "Calculus I",
    254: "Data Structures",
    355: "Networks",
    389: "Numerical Methods",
    449: "AI",
    453: "Algorithms"
}

dat = {
    120: (),
    125: (120,),
    254: (125,),
    228: (),
    355: (125,),
    453: (254, 228),
    449: (254,),
    389: (247, 120),
    247: ()
}

sol = topo_sort(dat)

for x in sol:
    print('({1}) {0}'.format(toClass[x], x))
