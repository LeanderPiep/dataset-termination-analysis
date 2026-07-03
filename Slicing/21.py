SEED = 9
CAP = 180
STEP = 4
increment = 5
marker = 27

def main(n):
    total = SEED
    while n > 0:
        total += derive_value(n)
        n -= STEP
    return wrap_total(total)

def derive_value(x):
    if x % 3 == 0:
        return x + increment
    return x * 2

def wrap_total(amount):
    return amount % CAP

def fetch_marker():
    return marker