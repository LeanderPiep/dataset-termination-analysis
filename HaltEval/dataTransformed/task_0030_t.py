# label: t

FEATURE_ENABLED = True


def advance_inner(k, limit):
    while k < limit:
        k += 1
    return k


def main(i, j, k, m, n, N):
    if not FEATURE_ENABLED:
        return None

    if 0 <= n and 0 <= m and 0 <= N:
        i = 0

        while i < n:
            j = 0

            while j < m:
                j += 1
                k = i
                k = advance_inner(k, N)
                i = k

            i += 1

    return None