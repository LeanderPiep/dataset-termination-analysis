def f(i):
    while i > 0 and i < 50:
        if i < 20:
            i = i-1
        if i > 10:
            i = i+1
        if 30 <= i and i <= 40:
            i = i-1
    return None