def greedy(c):
    s = set()

    while c and not solution(s):
        x = select(c)
        c.remove(x)

        if feasible(s, x):
            s.add(x)

    return s if solution(s) else None
