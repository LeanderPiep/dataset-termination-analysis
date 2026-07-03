LOW = 1
HIGH = 110
STEP = 3
shift = 7
pool = 12

def main(n):
    result = LOW
    for i in range(n):
        if i % 2 == 0:
            result += create_even_part(i)
        else:
            result += create_odd_part(i)
    return adjust_result(result)

def create_even_part(value):
    return value + shift

def create_odd_part(value):
    return value // 2

def adjust_result(amount):
    if amount > HIGH:
        return HIGH
    return amount

def inspect_pool():
    return pool