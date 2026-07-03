def f(A, B):
    if B >= (0x7fffffff * 2 + 1)//2: return None
    if B < 1: return None
    if A >= (0x7fffffff * 2 + 1)//2: return None
    q = 0
    r = A
    b = B
    if r < b:
        while A == q * b + r:
            if 2 * (b // 2) == b:
                q = 2 * q
                b = b // 2
                if r >= b:
                    q = q + 1
                    r = r - b
    return None