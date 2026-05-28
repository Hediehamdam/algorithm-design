def fractional_knapsack(weights, values, capacity):
    items = list(zip(weights, values))
    items.sort(key=lambda x: x[1] / x[0], reverse=True)

    total_value = 0

    for w, v in items:
        if capacity >= w:
            capacity -= w
            total_value += v
        else:
            total_value += v * (capacity / w)
            break

    return total_value
