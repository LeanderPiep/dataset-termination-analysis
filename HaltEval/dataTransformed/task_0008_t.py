# label: t

FEATURE_ENABLED = True


def normalize_inputs(a, b):
    return a, b


def reduce_values(a, b):
    if a > b:
        a -= b
    else:
        b -= a
    return a, b


def compute_until_equal(a, b):
    if a > 0 and b > 0:
        while a != b:
            a, b = reduce_values(a, b)
    return None


def main(value_a, value_b):
    if not FEATURE_ENABLED:
        return None

    a, b = normalize_inputs(value_a, value_b)
    return compute_until_equal(a, b)