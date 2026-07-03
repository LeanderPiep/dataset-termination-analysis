def f(i, j, m, n):
    if m > 0 and n > m:
        i = 0
        j = 0
        while i < n:
            if j < m:
                j += 1
            else:
                j = 0
                i += 1
    return None