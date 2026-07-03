def f(i, j):
    t = 0
    while i > 0 and j > 0:
        if i < j:
            t = i
            i = j
            j = t
        else:
            if i > j:
                j = i
            else:
                i = i-1
    return None