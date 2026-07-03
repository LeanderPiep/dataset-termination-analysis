def f(x, y):
    if x < -2147483647:
        return None
    if y < -2147483647:
        return None
    while True:
        oldx = x
        x = -y
        y = oldx
    return None