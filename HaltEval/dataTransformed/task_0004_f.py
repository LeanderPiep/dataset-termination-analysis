# label: f

FEATURE_ENABLED = True

def update_offset(value):
    return value - 2

def process_offset(value):
    while value != 0:
        value = update_offset(value)
    return None

def main(initial_value):
    if not FEATURE_ENABLED:
        return None

    return process_offset(initial_value)