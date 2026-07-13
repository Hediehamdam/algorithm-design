import math

def prim(graph):

    n = len(graph)

    selected = [False] * n
    key = [math.inf] * n
    parent = [-1] * n

    key[0] = 0

    for _ in range(n):

        u = -1
        minimum = math.inf

        for i in range(n):
            if not selected[i] and key[i] < minimum:
                minimum = key[i]
                u = i

        selected[u] = True

        for v in range(n):

            if graph[u][v] != 0 and not selected[v]:

                if graph[u][v] < key[v]:
                    key[v] = graph[u][v]
                    parent[v] = u

    return parent


if __name__ == "__main__":

    graph = [
        [0, 2, 0, 6, 0],
        [2, 0, 3, 8, 5],
        [0, 3, 0, 0, 7],
        [6, 8, 0, 0, 9],
        [0, 5, 7, 9, 0]
    ]

    print("Parent Array:")
    print(prim(graph))
