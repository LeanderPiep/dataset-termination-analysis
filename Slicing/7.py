LIMIT = 50
OFFSET = 3
multiplier = 2
fallback_value = 999

def main(x):
    result = 0
    for i in range(x):
        if i % 2 == 0:
            result += compute_even_product(i)
        elif i % 3 == 0:
            result += adjust_with_limit(i)
        else:
            result += add_offset(i)
    return result

def get_status_message():
    return "Running"

def compute_even_product(n):
    return n * multiplier

def add_offset(n):
    return n + OFFSET

def adjust_with_limit(n):
    if n > LIMIT:
        return LIMIT
    return n * 2

def get_fallback_value():
    temp = 123
    return fallback_value