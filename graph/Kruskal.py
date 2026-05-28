def kruskal(edges, n):
    edges.sort(key=lambda x: x[2])  # sort by weight
    parent = list(range(n))

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(a, b):
        parent[find(a)] = find(b)

    mst = []

    for u, v, w in edges:
        if find(u) != find(v):
            union(u, v)
            mst.append((u, v, w))

        if len(mst) == n - 1:
            break

    return mst
