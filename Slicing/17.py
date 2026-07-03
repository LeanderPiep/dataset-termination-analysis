START_POINT = 3
BOUNDARY = 140
STEP_WIDTH = 6
BOOST = 10
memo = 21

def main(n):
    total = START_POINT
    for index in range(n):
        total += calculate_segment(index)
    return reduce_total(total)

def calculate_segment(value):
    if value % 4 == 0:
        return value + BOOST
    elif value % 3 == 0:
        return value // 3
    return value + STEP_WIDTH

def reduce_total(amount):
    if amount > BOUNDARY:
        return BOUNDARY
    return amount

def read_memo():
    return memo