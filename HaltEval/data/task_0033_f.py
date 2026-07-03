def f(x, y):
    while x > 0 and y < 0:
        if x > y:
            y = ~x
        else:
            x = x - 1
    return None