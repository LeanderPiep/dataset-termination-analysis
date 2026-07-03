# label: f

FEATURE_ENABLED = True

def loop_condition(a, b, p, q, x, y):
    return q + a * b * p == x * y

def update_case1(a, b, p, q):
    a = a // 2
    b = b // 2
    p = 4 * p
    return a, b, p, q

def update_case2(a, b, p, q):
    a = a - 1
    q = q + b * p
    return a, b, p, q

def update_case3(a, b, p, q):
    b = b - 1
    q = q + a * p
    return a, b, p, q

def update_case4(a, b, p, q):
    a = a - 1
    b = b - 1
    q = q + (a + b + 1) * p
    return a, b, p, q

def main(x, y):
    if not FEATURE_ENABLED:
        return None

    if y < 1:
        return None

    a = x
    b = y
    p = 1
    q = 0

    while loop_condition(a, b, p, q, x, y):
        if a % 2 == 0 and b % 2 == 0:
            a, b, p, q = update_case1(a, b, p, q)
        elif a % 2 == 1 and b % 2 == 0:
            a, b, p, q = update_case2(a, b, p, q)
        elif a % 2 == 0 and b % 2 == 1:
            a, b, p, q = update_case3(a, b, p, q)
        else:
            a, b, p, q = update_case4(a, b, p, q)
    return None