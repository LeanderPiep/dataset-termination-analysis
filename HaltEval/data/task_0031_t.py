def f(q, p):
    while q > 0 and p > 0:
        if q < p:
            q = q - 1
        else:
            if p < q:
                p = p - 1
            else:
                break
    return None