START = 0
LIMIT = 130
STEP = 5
factor = 6
saved_state = 101

def main(n):
    result = START
    for idx in range(n):
        result += route_value(idx)
    return limit_result(result)

def route_value(number):
    if number % 2 == 0:
        return amplify(number)
    if number % 5 == 0:
        return reduce_number(number)
    return number + STEP

def amplify(value):
    return value * factor

def reduce_number(value):
    return value // 5

def limit_result(amount):
    if amount > LIMIT:
        return LIMIT
    return amount

def get_saved_state():
    return saved_state