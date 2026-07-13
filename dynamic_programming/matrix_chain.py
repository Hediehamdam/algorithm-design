# Algorithm: Matrix Chain Multiplication
# Time Complexity: O(n^3)
# Space Complexity: O(n^2)

def matrix_chain_order(p):
    n = len(p) - 1

    m = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    for L in range(2, n + 1):
        for i in range(1, n - L + 2):
            j = i + L - 1
            m[i][j] = float("inf")

            for k in range(i, j):
                q = (
                    m[i][k]
                    + m[k + 1][j]
                    + p[i - 1] * p[k] * p[j]
                )

                if q < m[i][j]:
                    m[i][j] = q

    return m[1][n]


if __name__ == "__main__":
    p = [30, 35, 15, 5, 10, 20, 25]
    print("Minimum Multiplications =", matrix_chain_order(p))
