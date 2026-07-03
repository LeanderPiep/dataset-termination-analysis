MIN_VALUE = 2
MAX_VALUE = 600
FACTOR = 4
SHIFT = 5
snapshot_metric = 71

def main(n):
    result = MIN_VALUE
    for current in range(n):
        result += transform_value(current)
        if result > MAX_VALUE:
            result = shrink_result(result)
    return wrap_result(result)

def transform_value(number):
    if number % 2 == 0:
        return compute_scaled_value(number)
    if number % 3 == 0:
        return compute_shifted_value(number)
    return number + SHIFT

def compute_scaled_value(value):
    return value * FACTOR + apply_adjustment(value)

def export_snapshot():
    total = snapshot_metric
    for i in range(4, 10):
        if i % 2 == 0:
            total += i * 2
        else:
            total -= i // 2
    return total

def compute_shifted_value(value):
    return value + SHIFT + apply_adjustment(value)

def apply_adjustment(v):
    if v % 5 == 0:
        return v // 5
    return v + 3

def shrink_result(amount):
    return amount // 2

def wrap_result(amount):
    return amount % MAX_VALUE

def describe_snapshot_state():
    if snapshot_metric > 60:
        return "high"
    return "normal"