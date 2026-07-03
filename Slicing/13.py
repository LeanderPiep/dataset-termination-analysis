LOWER = 0
UPPER = 90
JUMP = 5
factor = 2
stored_value = 300

def main(n):
    total = LOWER
    for index in range(n):
        if index % 3 == 0:
            total += handle_multiple(index)
        else:
            total += handle_regular(index)
    return clamp_result(total)

def handle_multiple(value):
    return value * factor

def handle_regular(value):
    return value + JUMP

def clamp_result(amount):
    if amount > UPPER:
        return UPPER
    return amount

def get_stored_value():
    return stored_value