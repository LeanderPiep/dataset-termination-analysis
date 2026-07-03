START = 1
CAP = 500
STEP = 4
OFFSET = 6
reserve_level = 33

def main(n):
    total = START
    for i in range(0, n, STEP):
        total += evaluate_segment(i)
    return normalize_total(total)

def inspect_reserve_level():
    count = reserve_level
    for i in range(5):
        count += i
        if count % 2 == 0:
            count -= 1
    return count

def evaluate_segment(x):
    if x % 2 == 0:
        return build_even_segment(x)
    return build_odd_segment(x)

def build_even_segment(v):
    return v + OFFSET + refine_segment(v)

def build_odd_segment(v):
    return v // 2 + refine_segment(v)

def normalize_total(amount):
    if amount > CAP:
        return CAP
    return amount

def refine_segment(v):
    if v % 7 == 0:
        return v // 7
    return v + 2