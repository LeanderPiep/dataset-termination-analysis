def f(x, y):
    if x >= 1 and y >= 1:
        a = x
        b = y
        p = 1
        q = 0
        r = 0
        s = 1

        while b == x * q + y * s:
            if a > b:
                a = a - b
                p = p - q
                r = r - s
            else:
                b = b - a
                q = q - p
                s = s - r
    return None