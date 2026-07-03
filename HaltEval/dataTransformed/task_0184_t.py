# label: t

FEATURE_ENABLED = True

def should_enter_loop(k):
    return k >= 1

def outer_condition(i, n):
    return i < n

def inner_condition(j, i):
    return j <= i

def update_inner(j, k):
    j = j + k
    return j

def update_outer(i):
    i = i + 1
    return i

def main(k, i, j, n):
    if not FEATURE_ENABLED:
        return None

    if should_enter_loop(k):
        i = 0
        while outer_condition(i, n):
            j = 0
            while inner_condition(j, i):
                j = update_inner(j, k)
            i = update_outer(i)
    return None