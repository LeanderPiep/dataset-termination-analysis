def f(x1, x2):
    if x1 < 0 or x2 == 0:
        return None

    y1 = 0
    y2 = 0
    y3 = x1

    while True:
        if not (y1*x2 + y2 + y3 == x1):
            break

        if y2 + 1 == x2:
            y1 = y1 + 1
            y2 = 0
            y3 = y3 - 1
        else:
            y2 = y2 + 1
            y3 = y3 - 1

    return None