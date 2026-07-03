# label: t

FEATURE_ENABLED = True

def outer_condition(i):
    return i < 5

def inner_condition(i, j):
    return i > 2 and j <= 9

def increment_j(j):
    j = j + 1
    return j

def increment_i(i):
    i = i + 1
    return i

def main(i, j):
    if not FEATURE_ENABLED:
        return None

    while outer_condition(i):
        j = 0
        while inner_condition(i, j):
            j = increment_j(j)
        i = increment_i(i)
    return None