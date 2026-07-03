LIMIT = 1000
FACTOR = 3
OFFSET = 7
BASE = 5
cache_value = 999

def main(n):
    result = BASE
    for i in range(n):
        if i % 2 == 0:
            result += compute_even_component(i)
        else:
            result += process_odd_sequence(i)
        if result > LIMIT:
            result = clamp_to_limit(result)
    return finalize_result(result)

def get_default_value():
    return 0

def compute_even_component(x):
    if x > OFFSET:
        return x * FACTOR
    else:
        return x + adjust_small_value(x)

def process_odd_sequence(y):
    total = y
    while total < LIMIT:
        total += compute_even_component(total) // 2
        if total % 5 == 0:
            total -= apply_correction(total)
    return total

def adjust_small_value(z):
    if z % 3 == 0:
        return z // 3 + apply_correction(z)
    return z + 1

def apply_correction(v):
    if v % 7 == 0:
        return v - 1
    return v + 2

def shift_value(val):
    return val - OFFSET

def clamp_to_limit(val):
    if val > LIMIT:
        return LIMIT
    return val

def finalize_result(final_result):
    return final_result % FACTOR

def get_cache_value():
    temp = 123
    return cache_value