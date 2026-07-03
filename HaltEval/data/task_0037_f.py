def f(i):
    up = 0
    while 0 <= i <= 10:
        if i == 10:
            up = 0
        if i == 0:
            up = 1
        if up == 1:
            i += 1
        else:
            i -= 1
    return None