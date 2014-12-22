def lamb(n):
    return [lambda j, i = q: i + j for q in range(n)]
