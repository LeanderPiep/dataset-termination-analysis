def f(y, z, x_choice):
    x = 1 if x_choice != 0 else -1
    while y < 100 and z < 100:
        y = y + x
        z = z - x
    return None