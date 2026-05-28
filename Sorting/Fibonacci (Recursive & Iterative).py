# Recursive Fibonacci
def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)


# Iterative Fibonacci
def fib_iterative(n):
    if n <= 1:
        return n

    f = [0] * (n + 1)
    f[0] = 0
    f[1] = 1

    for i in range(2, n + 1):
        f[i] = f[i - 1] + f[i - 2]

    return f[n]
