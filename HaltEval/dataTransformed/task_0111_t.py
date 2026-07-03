# label: t

FEATURE_ENABLED = True

def outer_condition(a):
    return a < 30

def inner_condition(b, a):
    return b < a

def update_inner(a, b):
    if b > 5:
        b = b + 7
    else:
        b = b + 2

    if b >= 10 and b <= 12:
        a = a + 10
    else:
        a = a + 1

    return a, b

def update_outer(a, b):
    a = a + 2
    b = b - 10
    return a, b

def main(a, b):
    if not FEATURE_ENABLED:
        return None

    while outer_condition(a):
        while inner_condition(b, a):
            a, b = update_inner(a, b)
        a, b = update_outer(a, b)
    return None