def f(n):
    def g(x, y):
        if x <= 23 and x >= -42:
            g(2*y-2, x + 1)
    if n <= 2147483646:
        g(n, n + 1)
    return None