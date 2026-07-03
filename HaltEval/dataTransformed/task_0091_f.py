# label: f

FEATURE_ENABLED = True

def initialize_state():
    return 0, 1, 1

def should_continue(total, current):
    return current * current - 4 * total + 2 * current + 1 == 0

def advance_state(counter, total, current):
    counter = counter + 1
    current = current + 2
    total = total + current
    return counter, total, current

def main(n):
    if not FEATURE_ENABLED:
        return None

    a, s, t = initialize_state()
    while should_continue(s, t):
        a, s, t = advance_state(a, s, t)
    return None