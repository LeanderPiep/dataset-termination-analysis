def f(x, y):
    if y < 1:
        return None

    a = x
    b = y
    p = 1
    q = 0

    while True:
        if q + a * b * p != x * y:
            break

        if a % 2 == 0 and b % 2 == 0:
            a = a // 2
            b = b // 2
            p = 4 * p
        elif a % 2 == 1 and b % 2 == 0:
            a = a - 1
            q = q + b * p
        elif a % 2 == 0 and b % 2 == 1:
            b = b - 1
            q = q + a * p
        else:
            a = a - 1
            b = b - 1
            q = q + (a + b + 1) * p

    return None