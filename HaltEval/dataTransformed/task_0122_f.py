# label: f

FEATURE_ENABLED = True

def should_exit_early(n):
    return n <= 0

def check_error(x):
    return x != 0

def loop_step(i):
    return i + 1

def main(n):
    if not FEATURE_ENABLED:
        return None

    i = 0
    x = 0
    y = 0

    if n > 0:
        while True:
            if check_error(x):
                return "error"
            i = loop_step(i)

    if x == 0:
        return "error"

    return None