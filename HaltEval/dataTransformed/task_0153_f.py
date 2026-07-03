# label: f

FEATURE_ENABLED = True

def precheck(a, b):
    return 1 <= a <= 65535 and 1 <= b <= 65535

def outer_condition(x, u, y, v, a, b):
    return x * u + y * v == a * b

def inner_loop1_condition(x, u, y, v, a, b):
    return x * u + y * v == a * b

def inner_loop2_condition(x, u, y, v, a, b):
    return x * u + y * v == a * b

def update_inner1(x, u, v, y):
    x = x - y
    v = v + u
    return x, v

def update_inner2(y, u, v, x):
    y = y - x
    u = u + v
    return y, u

def main(a, b):
    if not FEATURE_ENABLED:
        return None

    if not precheck(a, b):
        return None

    x = a
    y = b
    u = b
    v = 0

    while outer_condition(x, u, y, v, a, b):
        while inner_loop1_condition(x, u, y, v, a, b):
            x, v = update_inner1(x, u, v, y)
        while inner_loop2_condition(x, u, y, v, a, b):
            y, u = update_inner2(y, u, v, x)

    return None