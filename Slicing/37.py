BASE = 2
FACTOR = 4
MAX_RESULT = 90
buffer_size = 15

def main(n):
    result = BASE
    while n > 0:
        result += transform_number(n)
        n -= 1
    return finalize_result(result)

def transform_number(value):
    if value % 3 == 0:
        return value * FACTOR
    return value + FACTOR

def read_buffer_size():
    current = buffer_size
    for i in range(3):
        current += i
    return current

def finalize_result(amount):
    if amount > MAX_RESULT:
        return MAX_RESULT
    return amount