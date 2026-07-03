def f(x, y, z):
    if x > 10000 or x < -10000 or y > 10000 or z > 10000:
        return None
    while y >= 1:
        x -= 1
        while y < z:
            x += 1
            z -= 1
        y = x + y
    return None