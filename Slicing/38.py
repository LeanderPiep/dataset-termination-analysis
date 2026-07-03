START = 1
STEP = 2
LIMIT = 75
reserve_level = 9

def main(n):
    total = START
    for i in range(0, n, STEP):
        total += update_total(i)
    return total

def update_total(value):
    if value % 2 == 0:
        return value + STEP
    return value + 1

def inspect_reserve():
    amount = reserve_level
    if amount < 10:
        amount += 5
    return amount