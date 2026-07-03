def f(a, b):
    if b < 1:
        return None
    x = a
    y = b
    z = 0
    while True:
        if z + x * y != a * b:
            break
        if y % 2 == 1:
            z += x
            y -= 1
        x *= 2
        y //= 2
    return None