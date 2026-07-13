# Algorithm: Sum of Subsets (Backtracking)

def sum_of_subsets(weights, target):

    n = len(weights)

    subset = []

    def solve(index, current_sum):

        if current_sum == target:
            print(subset)
            return

        if index == n or current_sum > target:
            return

        subset.append(weights[index])
        solve(index + 1, current_sum + weights[index])

        subset.pop()
        solve(index + 1, current_sum)

    solve(0, 0)


if __name__ == "__main__":

    weights = [5, 10, 12, 13, 15, 18]
    target = 30

    sum_of_subsets(weights, target)
