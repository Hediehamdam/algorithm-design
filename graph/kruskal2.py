def find(parent, i):

    if parent[i] == i:
        return i

    return find(parent, parent[i])


def union(parent, rank, x, y):

    xroot = find(parent, x)
    yroot = find(parent, y)

    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot

    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot

    else:
        parent[yroot] = xroot
        rank[xroot] += 1


def kruskal(vertices, edges):

    result = []

    edges = sorted(edges, key=lambda item: item[2])

    parent = []
    rank = []

    for node in range(vertices):
        parent.append(node)
        rank.append(0)

    e = 0
    i = 0

    while e < vertices - 1:

        u, v, w = edges[i]
        i += 1

        x = find(parent, u)
        y = find(parent, v)

        if x != y:
            e += 1
            result.append((u, v, w))
            union(parent, rank, x, y)

    return result


if __name__ == "__main__":

    vertices = 4

    edges = [
        (0, 1, 10),
        (0, 2, 6),
        (0, 3, 5),
        (1, 3, 15),
        (2, 3, 4)
    ]

    mst = kruskal(vertices, edges)

    print("Minimum Spanning Tree:")

    for edge in mst:
        print(edge)
