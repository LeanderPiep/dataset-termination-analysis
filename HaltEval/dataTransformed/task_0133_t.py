# label: t

FEATURE_ENABLED = True

def outer_condition(i):
    return i > 0

def inner_condition(j):
    return j > 0

def update_inner(j):
    j = j - 1
    return j

def update_outer(i):
    i = i - 1
    return i

def main(N):
    if not FEATURE_ENABLED:
        return None

    i = N
    while outer_condition(i):
        j = N
        while inner_condition(j):
            j = update_inner(j)
        i = update_outer(i)
    return None