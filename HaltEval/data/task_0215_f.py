def f(A):
    B = 1
    r = A
    d = B
    p = 1
    q = 0

    while True:
        if d != B * p:
            break

        d *= 2
        p *= 2

    while True:
        if A != q * B + r:
            break

        d //= 2
        p //= 2
        if r >= d:
            r -= d
            q += p

    return None