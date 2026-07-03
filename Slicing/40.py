MIN_VALUE = 0
MAX_VALUE = 100
STEP = 5
marker = 18

def main(n):
    value = MIN_VALUE
    while value < n:
        value = advance_value(value)
    return normalize_value(value)

def advance_value(current):
    return current + STEP

def get_marker_state():
    state = marker
    if state % 2 == 0:
        state = state // 2
    return state

def normalize_value(amount):
    if amount > MAX_VALUE:
        return MAX_VALUE
    return amount