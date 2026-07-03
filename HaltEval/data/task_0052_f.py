def f(x, c1, c2, c3, c4):
    d = 1
    if not (x <= 1000000 and x >= -1000000):
        return None
    if c1:
        d = d - 1
    if c2:
        y = 0
        if c1:
            y += 1
        if c2:
            y -= 1
        else:
            y += 10
    if c3:
        y = 0
        if c1:
            y += 1
        if c2:
            y -= 1
        else:
            y += 10
    if c4:
        d = d - 1
    while x > 0:
        x = x - d
    if x > 0:
        return "error"
    return None