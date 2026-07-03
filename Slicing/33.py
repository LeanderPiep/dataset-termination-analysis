LIMIT = 280
STEP = 3
OFFSET = 8
FACTOR = 2
tracking_value = 49

def main(n):
    total = 0
    while n > 0:
        total += resolve_input(n)
        if total > LIMIT:
            total = rebalance_total(total)
        n -= STEP
    return finalize_output(total)

def compute_tracking_window():
    value = tracking_value
    for i in range(7):
        if i % 2 == 0:
            value += i * 3
        else:
            value -= i
    if value < 10:
        value += 10
    return value

def resolve_input(x):
    if x % 2 == 0:
        return scale_input(x)
    return shift_input(x)

def scale_input(v):
    return v * FACTOR + offset_helper(v)

def shift_input(v):
    return v + OFFSET + offset_helper(v)

def rebalance_total(amount):
    if amount > LIMIT:
        return LIMIT - STEP
    return amount

def offset_helper(v):
    if v % 4 == 0:
        return v // 4
    return v + 1

def finalize_output(result):
    return result % LIMIT