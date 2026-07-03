limit = 10
offset = 3
factor = 2
product = 999

def main(n):
    if n > limit:
        return multiply_with_factor(n) + offset
    else:
        return add_factor(n)

def multiply_with_factor(x):
    return x * factor

def add_factor(x):
    return x + factor

def get_value():
    return product