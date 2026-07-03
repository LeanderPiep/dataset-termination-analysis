def f(x, y):
    a = 0
    while x < 0:
        if x < 0 and y >= 0:
            x = ~y
        else:
            x = x - 1
    return None