# Algorithm: Traveling Salesman Problem (Held-Karp)
# Dynamic Programming
# Time Complexity: O(n^2 * 2^n)
# Space Complexity: O(n * 2^n)

from functools import lru_cache

def tsp(graph):

    n = len(graph)

    @lru_cache(None)
    def dp(mask, pos):

        if mask == (1 << n) - 1:
            return graph[pos][0]

        ans = float("inf")

        for city in range(n):

            if (mask & (1 << city)) == 0:

                ans = min(
                    ans,
                    graph[pos][city] +
                    dp(mask | (1 << city), city)
                )

        return ans

    return dp(1, 0)


if __name__ == "__main__":

    graph = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]

    print("Minimum Cost =", tsp(graph))
