START = 0
UPPER_BOUND = 100

def main(n):
    return calculate_sum(n)

def calculate_sum(n):
    total = START
    for i in range(n):
        total += i
    return total

def sum_until_upper_bound():
    return calculate_sum(UPPER_BOUND)