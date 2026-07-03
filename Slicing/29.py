LIMIT = 450
STEP = 3
OFFSET = 4
FACTOR = 2
cache_value = 91

def main(n):
    total = 0
    for i in range(n):
        if i % 2 == 0:
            total += compute_even_path(i)
        else:
            total += compute_odd_path(i)
        if total > LIMIT:
            total = clamp_total(total)
    return finalize_total(total)

def summarize_cache():
    result = cache_value
    for i in range(6):
        if i % 2 == 0:
            result += i * 2
        else:
            result -= i
    if result < 0:
        result = abs(result)
    return result

def compute_even_path(value):
    return value * FACTOR + adjust_value(value)

def compute_odd_path(value):
    return value + OFFSET + adjust_value(value)

def adjust_value(x):
    if x % 5 == 0:
        return x // 5
    return x // 2

def clamp_total(amount):
    if amount > LIMIT:
        return LIMIT
    return amount

def finalize_total(result):
    return result % LIMIT