def f(x, y):
    a = 0
    while y > 0:
        if x < 0:
            y = ~x
        else:
            y = y - 1
    return None