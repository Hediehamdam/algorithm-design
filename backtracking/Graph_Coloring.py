# Algorithm: Graph Coloring (Backtracking)
# Time Complexity: O(m^n)

def promising(v, graph, color):
    for i in range(len(graph)):
        if graph[v][i] and color[v] == color[i]:
            return False
    return True


def graph_coloring(graph, m, color, v):

    if v == len(graph):
        print(color)
        return

    for c in range(1, m + 1):

        color[v] = c

        if promising(v, graph, color):
            graph_coloring(graph, m, color, v + 1)

        color[v] = 0


if __name__ == "__main__":

    graph = [
        [0,1,1,1],
        [1,0,1,0],
        [1,1,0,1],
        [1,0,1,0]
    ]

    m = 3

    color = [0] * len(graph)

    graph_coloring(graph, m, color, 0)
