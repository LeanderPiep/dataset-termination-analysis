BASE = 5
STEP = 2
LIMIT = 300
FACTOR = 3
backup_metric = 44

def main(n):
    value = BASE
    while n > 0:
        value += process_number(n)
        n -= STEP
    return normalize(value)

def process_number(x):
    if x % 4 == 0:
        return multiply_component(x)
    elif x % 3 == 0:
        return reduce_component(x)
    return x + FACTOR

def multiply_component(v):
    return v * FACTOR

def reduce_component(v):
    return v // 3 + adjust_component(v)

def adjust_component(v):
    if v % 5 == 0:
        return v // 5
    return v + 1

def normalize(value):
    return value % LIMIT

def analyze_backup():
    result = backup_metric
    for i in range(10):
        if i % 3 == 0:
            result += i * 2
        else:
            result -= i
    if result < 0:
        result = abs(result)
    return result