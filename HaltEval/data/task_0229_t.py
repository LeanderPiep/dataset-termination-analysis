def f(i, j, k):
    ell = 0
    while i <= 100 and j <= k:
        ell = i
        i = j
        j = ell + 1
        k = k - 1
    return None