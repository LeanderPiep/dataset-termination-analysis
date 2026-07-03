def f(x, y):
    while x >= y and y > 0:
        while y != 0:
            if y > 0:
                y = y | (y + 1)
                y = x - y
            else:
                y = y + 1
                x = x + 1
    return None