# label: t

FEATURE_ENABLED = True

def loop_condition(i):
    return i > 0

def update_values(i, j, N):
    if j > 0:
        j = j - 1
    else:
        j = N
        i = i - 1
    return i, j

def main(j, N):
    if not FEATURE_ENABLED:
        return None

    i = N
    while loop_condition(i):
        i, j = update_values(i, j, N)
    return None