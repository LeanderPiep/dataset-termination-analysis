def f(x, y):
    a = 1
    while x != 0 and y != 0:
        a = x
        x = y
        y = ~a
    return None