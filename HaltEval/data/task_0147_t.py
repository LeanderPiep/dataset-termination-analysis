def f(a, b, x, y):
    if a == b + 1 and x < 0:
        while x >= 0 or y >= 0:
            x = x + a - b - 1
            y = y + b - a - 1
    return None