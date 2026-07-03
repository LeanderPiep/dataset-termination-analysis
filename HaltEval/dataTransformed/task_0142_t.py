# label: t

FEATURE_ENABLED = True

def is_loop_applicable(c):
    return c >= 2

def loop_condition(x, c):
    return x + c >= 0

def decrement_and_increment(x, c):
    x = x - c
    c = c + 1
    return x, c

def main(x, c):
    if not FEATURE_ENABLED:
        return None

    if is_loop_applicable(c):
        while loop_condition(x, c):
            x, c = decrement_and_increment(x, c)
    return None