def f(x, y):
    a = x
    b = y
    p = 1
    q = 0
    r = 0
    s = 1

    while b != 0:
        c = a
        k = 0

        while c >= b:
            d = 1
            v = b

            while b == x * q + y * s:
                d = 2 * d
                v = 2 * v

            c = c - v
            k = k + d

        a = b
        b = c
        temp = p
        p = q
        q = temp - q * k
        temp = r
        r = s
        s = temp - s * k

    return None