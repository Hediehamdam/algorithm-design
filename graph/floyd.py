floyd(graph):
    n = len(graph)

    dist = []

    for i in range(n):
        dist.append(graph[i][:])

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist


if __name__ == "__main__":

    INF = float("inf")

    graph = [
        [0, 5, INF, 10],
        [INF, 0, 3, INF],
        [INF, INF, 0, 1],
        [INF, INF, INF, 0]
    ]

    result = floyd(graph)

    print("Shortest Path Matrix:")
    for row in result:
        print(row)
