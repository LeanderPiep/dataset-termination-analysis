def f(n, m):
    if m > 0 and n > m:
        i = n
        while i > 0:
            if i < m:
                i -= 1
            else:
                i -= m
    return None