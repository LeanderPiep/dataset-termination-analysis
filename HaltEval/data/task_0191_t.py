def f(i, j, k, tmp):
    while i <= 100 and j <= k:
        tmp, i, j, k = i, j, tmp + 1, k - 1
    return None