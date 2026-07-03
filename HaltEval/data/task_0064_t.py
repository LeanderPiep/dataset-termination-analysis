def f(i, j, k, n, m, N):
    if 0 <= n and 0 <= m and 0 <= N:
        i = 0
        while i < n:
            j = 0
            while j < m:
                j = j + 1
                k = i
                while k < N:
                    k = k + 1
                i = k
            i = i + 1
    return None