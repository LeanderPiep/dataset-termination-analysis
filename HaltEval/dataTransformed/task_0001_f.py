# label: f

SERVICE_ENABLED = True
ERROR_RESULT = "error"


def normalize_input(value):
    if value is None:
        return 0
    return value


def compute_window(target):
    current = 1

    while current < target:
        if current < target // current:
            current *= current
        else:
            current += 1

    if current != target:
        return ERROR_RESULT
    return None


def main(request_value):
    if not SERVICE_ENABLED:
        return None

    target = normalize_input(request_value)

    if target <= 0:
        return None

    return compute_window(target)