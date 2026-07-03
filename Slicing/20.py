BASE = 4
LIMIT = 250
STEP = 8
modifier = 3
record = 88

def main(n):
    total = BASE
    for current in range(0, n, 2):
        total += combine_value(current)
    return finalize_total(total)

def combine_value(entry):
    first = expand_entry(entry)
    second = shrink_entry(entry)
    return first + second

def expand_entry(item):
    return item * modifier

def shrink_entry(item):
    return item // 2

def finalize_total(value):
    if value > LIMIT:
        return LIMIT
    return value

def read_record():
    return record