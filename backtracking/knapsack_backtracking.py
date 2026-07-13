# Algorithm: 0/1 Knapsack (Backtracking)

max_profit = 0
best_set = []


def knapsack(weights, profits, capacity):

    global max_profit, best_set

    n = len(weights)

    include = [0] * n

    def solve(i, profit, weight):

        global max_profit, best_set

        if weight <= capacity and profit > max_profit:
            max_profit = profit
            best_set = include[:]

        if i == n:
            return

        if weight > capacity:
            return

        include[i] = 1
        solve(
            i + 1,
            profit + profits[i],
            weight + weights[i]
        )

        include[i] = 0
        solve(i + 1, profit, weight)

    solve(0, 0, 0)

    return max_profit, best_set


if __name__ == "__main__":

    weights = [2, 5, 10, 5]
    profits = [40, 30, 50, 10]
    capacity = 16

    profit, solution = knapsack(
        weights,
        profits,
        capacity
    )

    print("Maximum Profit:", profit)
    print("Selected Items:", solution)
