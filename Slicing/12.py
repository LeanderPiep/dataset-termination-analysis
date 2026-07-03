BASE = 10
STEP = 3
CAP = 150
delta = 6
archive = 77

def main(n):
    current = BASE
    for i in range(0, n, STEP):
        current += evaluate_branch(i)
    return finalize(current)

def evaluate_branch(item):
    if item % 4 == 0:
        return scale_value(item)
    return shift_value(item)

def scale_value(number):
    return number * delta

def shift_value(number):
    return number + STEP

def finalize(value):
    if value > CAP:
        return CAP
    return value

def read_archive():
    return archive