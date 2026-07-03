def f(x, y):
    if x >= 0 and y >= 0:
        while x - y > 2 or y - x > 2:
            if x < y:
                x += 1
            else:
                y += 1
    return None