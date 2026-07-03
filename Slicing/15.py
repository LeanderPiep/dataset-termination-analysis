MIN_VALUE = 1
MAX_VALUE = 75
STEP = 4
rate = 3
snapshot = 18

def main(n):
    total = 0
    for i in range(MIN_VALUE, n, STEP):
        total += build_piece(i)
    return finish_total(total)

def build_piece(item):
    if item % 2 == 0:
        return item * rate
    return item + rate

def finish_total(value):
    while value > MAX_VALUE:
        value -= STEP
    return value

def get_snapshot():
    return snapshot