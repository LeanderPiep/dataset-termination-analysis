THRESHOLD = 300
BASE = 2
STEP = 5
FACTOR = 2
backup_number = 64

def main(n):
    total = BASE
    while total < THRESHOLD:
        total += expand_value(n)
        n -= 1
        if n <= 0:
            break
    return total

def expand_value(value):
    if value % 2 == 0:
        return value * FACTOR
    return value + STEP

def get_backup_number():
    return backup_number

def reset_value():
    return BASE