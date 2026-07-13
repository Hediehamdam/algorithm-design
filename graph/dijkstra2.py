import math

def dijkstra(graph, start):

    n = len(graph)

    visited = [False] * n
    distance = [math.inf] * n
    parent = [-1] * n

    distance[start] = 0

    for _ in range(n):

        u = -1
        minimum = math.inf

        for i in range(n):
            if not visited[i] and distance[i] < minimum:
                minimum = distance[i]
                u = i

        if u == -1:
            break

        visited[u] = True

        for v in range(n):

            if graph[u][v] != 0 and graph[u][v] != math.inf:

                if distance[u] + graph[u][v] < distance[v]:
                    distance[v] = distance[u] + graph[u][v]
                    parent[v] = u

    return distance, parent


if __name__ == "__main__":

    INF = math.inf

    graph = [
        [0, 4, 2, INF],
        [4, 0, 5, 10],
        [2, 5, 0, 3],
        [INF, 10, 3, 0]
    ]

    distance, parent = dijkstra(graph, 0)

    print("Distance:", distance)
    print("Parent:", parent)
