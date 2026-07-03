MIN_VALUE = 2
MAX_VALUE = 400
STEP = 3
OFFSET = 7
archive_data = 123

def main(n):
    result = MIN_VALUE
    for i in range(n):
        if i % 2 == 0:
            result += transform_even(i)
        else:
            result += transform_odd(i)
        if result > MAX_VALUE:
            result = compress_result(result)
    return result

def transform_even(v):
    return v * STEP + adjust_even(v)

def transform_odd(v):
    return v + OFFSET + adjust_odd(v)

def adjust_even(x):
    if x % 5 == 0:
        return x // 5
    return x // 2

def adjust_odd(x):
    if x % 3 == 0:
        return x // 3
    return x + 2

def compress_result(val):
    return val % MAX_VALUE

def process_archive():
    total = archive_data
    for i in range(6):
        if i % 2 == 0:
            total += i * 3
        else:
            total -= i
    if total > 200:
        total = total // 2
    return total