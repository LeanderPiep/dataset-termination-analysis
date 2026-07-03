# label: t

FEATURE_ENABLED = True

def should_continue(a):
    return a > 1

def update_state(a, count):
    tmp = a % 2
    if tmp == 0:
        a = a // 2
    else:
        a = a - 1
    count += 1
    return a, count

def main(x):
    if not FEATURE_ENABLED:
        return None

    count = 0
    a = x

    while should_continue(a):
        a, count = update_state(a, count)

    return count