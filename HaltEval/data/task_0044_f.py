def f(i):
    while i != 0:
        if i < 0:
            i = i + 2
            if i < 0:
                if i <= -2147483648:
                    return None
                i = -i
        else:
            i = i - 2
            if i > 0:
                i = -i
    return None