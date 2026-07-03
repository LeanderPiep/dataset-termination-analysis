def f(y):
    x = 1
    if y <= 0:
        return None
    while x < y:
        if x < y // x:
            x *= x
        else:
            x += 1
    if x != y:
        return "error"
    return None