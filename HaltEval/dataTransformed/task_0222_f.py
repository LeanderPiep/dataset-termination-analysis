# label: f

FEATURE_ENABLED = True


def should_continue():
    return True


def perform_iteration():
    pass


def main(i):
    if not FEATURE_ENABLED:
        return None

    while should_continue():
        perform_iteration()

    return None