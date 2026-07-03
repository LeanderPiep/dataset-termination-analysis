def f(x):
    def g(x):
        if x == 0:
            return 1
        else:
            return g(g(x - 1) + 1)
    if x >= 0:
        g(x)
    return None