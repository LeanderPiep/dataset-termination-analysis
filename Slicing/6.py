MAX = 100
MIN = 1
STEP = 5
factor = 2
backup_value = 999

def main(n):
    total = 0
    for i in range(MIN, n, STEP):
        if i % 2 == 0:
            total += process_even_number(i)
        else:
            total += process_odd_number(i)
    while total < MAX:
        total = increase_until_limit(total)
    return total

def process_even_number(x):
    return x * factor + increase_until_limit(x)

def process_odd_number(x):
    if x % 3 == 0:
        return x // 2
    else:
        return x + factor

def increase_until_limit(value):
    if value >= MAX:
        return value
    return value + STEP

def get_backup_value():
    temp = 42
    return backup_value