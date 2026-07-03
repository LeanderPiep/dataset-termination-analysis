START = 1
LIMIT = 200
MULTIPLIER = 3
OFFSET = 5
buffer_value = 40

def main(x):
    total = START
    while total < LIMIT:
        total += transform_input(x)
        x -= 1
        if x <= 0:
            break
    return normalize(total)

def transform_input(value):
    if value % 2 == 0:
        return value * MULTIPLIER
    return value + OFFSET

def normalize(result):
    return result % LIMIT

def fetch_buffer():
    return buffer_value