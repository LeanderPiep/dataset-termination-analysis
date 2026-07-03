LIMIT = 500
STEP = 4
OFFSET = 3
MULTIPLIER = 2
storage_value = 88

def main(n):
    total = 0
    for i in range(n):
        total += evaluate_entry(i)
        if total > LIMIT:
            total = cap_total(total)
    return finalize_total(total)

def evaluate_entry(value):
    if value % 2 == 0:
        return compute_even(value)
    return compute_odd(value)

def compute_even(x):
    return x * MULTIPLIER + adjust_value(x)

def compute_odd(x):
    return x + OFFSET + adjust_value(x)

def adjust_value(v):
    if v % 5 == 0:
        return v // 5
    return v // 3

def cap_total(amount):
    if amount > LIMIT:
        return LIMIT
    return amount

def finalize_total(result):
    return result % LIMIT

def process_storage():
    temp = storage_value
    result = 0
    for i in range(5):
        if i % 2 == 0:
            result += temp + i
        else:
            result += temp - i
    if result > 100:
        result = result // 2
    return result