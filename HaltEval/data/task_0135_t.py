
def f(x, y):
    if not (x >= 0 and y >= 0):
        return None
    if y == 0:
        return x
    else:
        if x == 0:
            return f(y, y-1)
        else:
            return f(y, x-1)
    return None
