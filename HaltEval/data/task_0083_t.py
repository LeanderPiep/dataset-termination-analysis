def f(x, y):
    if x < 0:
        x = -x
    if y < 0:
        y = -y
    while y > 0:
        r = x
        while r >= y:
            r = r - y
        x = y
        y = r
    return None