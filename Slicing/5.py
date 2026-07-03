base = 0
decrement = 1

def main(n):
    if is_base_case(n):
        return n
    return main(n - decrement)

def is_base_case(x):
    return x <= base

def get_decrement():
    return decrement