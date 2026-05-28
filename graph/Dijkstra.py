import math

def dijkstra(graph, src):
    n = len(graph)
    dist = [math.inf] * n
    visited = [False] * n
    parent = [-1] * n

    dist[src] = 0

    for _ in range(n):
        u = min((d, i) for i, d in enumerate(dist) if not visited[i])[1]
        visited[u] = True

        for v in range(n):
            if graph[u][v] and not visited[v]:
                if dist[v] > dist[u] + graph[u][v]:
                    dist[v] = dist[u] + graph[u][v]
                    parent[v] = u

    return dist, parent
