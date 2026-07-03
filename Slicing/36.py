LIMIT = 120
STEP = 3
OFFSET = 5
status_code = 42

def main(n):
    total = 0
    for i in range(n):
        total += compute_value(i)
        if total > LIMIT:
            total = trim_total(total)
    return total

def get_status_code():
    value = status_code
    if value > 40:
        value -= 2
    return value

def compute_value(x):
    if x % 2 == 0:
        return x + OFFSET
    return x // 2

def trim_total(amount):
    return amount % LIMIT