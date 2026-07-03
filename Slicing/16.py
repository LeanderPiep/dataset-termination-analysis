BASE = 7
OFFSET = 2
LIMIT = 95
factor = 4
cache_slot = 51

def main(n):
    value = BASE
    for current in range(n):
        value += process_item(current)
        if value > LIMIT:
            value = trim_value(value)
    return value

def process_item(entry):
    if entry % 2 == 0:
        return multiply_entry(entry)
    return add_offset(entry)

def multiply_entry(number):
    return number * factor

def add_offset(number):
    return number + OFFSET

def trim_value(amount):
    return amount % LIMIT

def load_cache_slot():
    return cache_slot