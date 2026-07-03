INITIAL = 5
STEP = 2
LIMIT = 120
EXTRA = 8
shadow = 999

def main(n):
    result = INITIAL
    while n > 0:
        result += compute_delta(n)
        n -= STEP
    return cap_value(result)

def compute_delta(value):
    if value % 5 == 0:
        return apply_bonus(value)
    return value + EXTRA

def apply_bonus(amount):
    return amount // STEP

def cap_value(number):
    if number > LIMIT:
        return LIMIT
    return number

def resolve_shadow():
    return shadow