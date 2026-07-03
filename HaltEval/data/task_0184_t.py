def f(k, i, j, n):
    if k >= 1:
        i = 0
        while i < n:
            j = 0
            while j <= i:
                j = j + k
            i = i + 1
    return None