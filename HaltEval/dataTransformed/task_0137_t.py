# label: t

FEATURE_ENABLED = True

def outer_condition(i, n):
    return i < n

def inner_condition(j, i):
    return j <= i

def update_inner(j):
    j = j + 1
    return j

def update_outer(i):
    i = i + 1
    return i

def main(i, j, n):
    if not FEATURE_ENABLED:
        return None

    while outer_condition(i, n):
        j = 0
        while inner_condition(j, i):
            j = update_inner(j)
        i = update_outer(i)
    return None