# label: t

FEATURE_ENABLED = True
THRESHOLD = 2


def adjust_values(a, b):
    if a < b:
        a += 1
    else:
        b += 1
    return a, b


def balance_until_close(a, b):
    if a >= 0 and b >= 0:
        while abs(a - b) > THRESHOLD:
            a, b = adjust_values(a, b)
    return None


def main(value_a, value_b):
    if not FEATURE_ENABLED:
        return None

    return balance_until_close(value_a, value_b)