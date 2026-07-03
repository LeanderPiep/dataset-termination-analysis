def f(x_nondet, y, z):
    if x_nondet != 0:
        x = 1
    else:
        x = -1
    if x > 0:
        x = x + 1
    else:
        x = x - 1
    if x > 0:
        x = x + 1
    else:
        x = x - 1
    if x > 0:
        x = x + 1
    else:
        x = x - 1
    if x > 0:
        x = x + 1
    else:
        x = x - 1
    if x > 0:
        x = x + 1
    else:
        x = x - 1
    if x > 0:
        x = x + 1
    else:
        x = x - 1
    if x > 0:
        x = x + 1
    else:
        x = x - 1
    if x > 0:
        x = x + 1
    else:
        x = x - 1
    while y < 100 and z < 100:
        y = y + x
        z = z - x
    return None