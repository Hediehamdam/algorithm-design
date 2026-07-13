# Algorithm: Factorial (Dynamic Programming)
# Time Complexity: O(n)
# Space Complexity: O(n)

def factorial_dp(n):
    f = [0] * (n + 1)
    f[0] = 1

    for i in range(1, n + 1):
        f[i] = f[i - 1] * i

    return f[n]


if __name__ == "__main__":
    n = int(input("Enter n: "))
    print("Factorial =", factorial_dp(n))
