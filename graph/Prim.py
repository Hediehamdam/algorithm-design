import math

def prim(cost, n):
    selected = [False] * n
    min_dist = [math.inf] * n
    parent = [-1] * n

    # start from vertex 0
    min_dist[0] = 0

    for _ in range(n):
        # find minimum distance vertex
        u = -1
        min_val = math.inf

        for i in range(n):
            if not selected[i] and min_dist[i] < min_val:
                min_val = min_dist[i]
                u = i

        selected[u] = True

        # update neighbors
        for v in range(n):
            if cost[u][v] and not selected[v] and cost[u][v] < min_dist[v]:
                min_dist[v] = cost[u][v]
                parent[v] = u

    return parent
