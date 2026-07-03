def f(x):
    if x == 0:
        return 0
    else:
        return f(f(x - 1))