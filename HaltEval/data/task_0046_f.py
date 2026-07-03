def f(x):
    def g(x):
        if x <= 0:
            return 0
        else:
            return f(x - 1) + f(x - 2)
    if x <= 0:
        return 0
    else:
        return g(x) + g(x + 1)
    return None