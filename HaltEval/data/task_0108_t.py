def f(i, j, k):
    while i <= 100 and j <= k:
        ell = i
        i = j
        j = ell + 1
        k -= 1
    return None