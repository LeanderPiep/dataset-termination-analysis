def f(i, j, k, m, n, N):
    if 0 <= n and 0 <= m and 0 <= N:
        i = 0
        while i < n:
            j = 0
            while j < m:
                j += 1
                k = i
                while k < N:
                    k += 1
                i = k
            i += 1
    return None