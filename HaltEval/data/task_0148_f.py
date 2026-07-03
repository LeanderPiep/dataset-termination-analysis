def f(i, j):
    t = 0
    while i != 0 and j != 0:
        t = i
        i = j
        j = t
    return None