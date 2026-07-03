def f(loop1, n1):
    sn = 0
    x = 0
    while True:
        sn += 2
        x += 1
        if not (sn == x * 2 or sn == 0):
            return "error"
    return None