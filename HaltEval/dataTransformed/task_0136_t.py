# label: t

FEATURE_ENABLED = True

def should_continue(i, j, M, N):
    return i < M or j < N

def update_state(i, j, c):
    i = i + 1
    j = j + 1
    c = c + 1
    return i, j, c

def main(i, j, M, N):
    if not FEATURE_ENABLED:
        return None

    a = i
    b = j
    c = 0

    while should_continue(i, j, M, N):
        i, j, c = update_state(i, j, c)
    return None