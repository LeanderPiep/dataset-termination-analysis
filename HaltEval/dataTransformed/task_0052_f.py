# label: f

FEATURE_ENABLED = True
BOUND = 1_000_000


def compute_step(c1, c2, c3, c4):
    step = 1

    if c1:
        step -= 1

    if c2:
        temp = 0
        if c1:
            temp += 1
        if c2:
            temp -= 1
        else:
            temp += 10

    if c3:
        temp = 0
        if c1:
            temp += 1
        if c2:
            temp -= 1
        else:
            temp += 10

    if c4:
        step -= 1

    return step


def main(x, c1, c2, c3, c4):
    if not FEATURE_ENABLED:
        return None

    if not (-BOUND <= x <= BOUND):
        return None

    step = compute_step(c1, c2, c3, c4)

    while x > 0:
        x = x - step

    if x > 0:
        return "error"

    return None