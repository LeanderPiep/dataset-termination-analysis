def f(x, y):
    while x >= 0:
        y = 1
        while y < x:
            y += 1
        x -= 1
    return None