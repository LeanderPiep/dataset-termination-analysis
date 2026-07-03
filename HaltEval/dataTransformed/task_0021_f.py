# label: f

FEATURE_ENABLED = True


def update_index(index):
    return index + 1


def main(initial_index):
    if not FEATURE_ENABLED:
        return None

    index = initial_index

    while index < 0:
        if index != -5:
            index = update_index(index)

    return None