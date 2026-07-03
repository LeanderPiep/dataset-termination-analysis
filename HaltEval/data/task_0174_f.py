def f(i):
    range = 20
    while 0 <= i and i <= range:
        if not (0 == i and i == range):
            if i == range:
                i = 0
                range -= 1
            else:
                i += 1
    return None