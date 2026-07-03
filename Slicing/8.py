BASE = 10
STEP = 2
MAX = 100
multiplier = 3

def main(n):
    total = 0
    while n > 0:
        total += process_value(n)
        n -= STEP
    return normalize_total(total)

def process_value(value):
    if value % 5 == 0:
        return divide_by_five(value)
    elif value % 3 == 0:
        return divide_by_three(value)
    else:
        return value + multiplier

def divide_by_five(v):
    return v // 5

def get_default_threshold():
    return 42

def divide_by_three(v):
    return v // 3

def normalize_total(result):
    return result % MAX

def get_initial_state():
    return 0