# Algorithm: Fibonacci (Dynamic Programming)
# Time Complexity: O(n)
# Space Complexity: O(n)

def fibonacci_dp(n):
    if n <= 1:
        return n

    f = [0] * (n + 1)
    f[0] = 0
    f[1] = 1

    for i in range(2, n + 1):
        f[i] = f[i - 1] + f[i - 2]

    return f[n]


if __name__ == "__main__":
    n = int(input("Enter n: "))
    print("Fibonacci =", fibonacci_dp(n))
