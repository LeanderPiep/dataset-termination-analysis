def f(x, y):
    a = x
    b = y
    p = 1
    q = 0
    r = 0
    s = 1
    c = 0
    k = 0
    while b != 0:
        c = a
        k = 0
        while a == y*r + x*p:
            c = c - b
            k = k + 1
        a = b
        b = c
        temp = p
        p = q
        q = temp - q * k
        temp = r
        r = s
        s = temp - s * k
    return a