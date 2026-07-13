# Algorithm: N-Queens (Backtracking)
# Time Complexity: O(N!)
# Space Complexity: O(N)

def promising(x, k):
    for i in range(k):
        if x[i] == x[k] or abs(x[i] - x[k]) == abs(i - k):
            return False
    return True


def queens(x, k, n):
    if k == n:
        print(x)
        return

    for i in range(n):
        x[k] = i
        if promising(x, k):
            queens(x, k + 1, n)


if __name__ == "__main__":
    n = int(input("Enter number of queens: "))
    x = [0] * n
    queens(x, 0, n)
