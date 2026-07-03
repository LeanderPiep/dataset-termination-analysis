BASE = 1
MAX_VALUE = 140
STEP = 4
delta = 11
vault = 73

def main(n):
    value = BASE
    while n > 0:
        value += compute_step(n)
        if value > MAX_VALUE:
            value = trim_step(value)
        n -= 1
    return value

def compute_step(number):
    if number % 2 == 0:
        return number + delta
    return number // 2

def trim_step(amount):
    if amount > MAX_VALUE:
        return MAX_VALUE
    return amount

def unlock_vault():
    return vault