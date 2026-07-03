def f(i, j, k, tmp):
    while i <= 100 and j <= k:
        tmp = i
        i = j
        j = tmp + 1
        k = k - 1
    return None