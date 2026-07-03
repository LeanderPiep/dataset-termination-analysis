INITIAL = 2
LIMIT = 90
STEP = 7
multiplier = 5
token = 19

def main(n):
    score = INITIAL
    for i in range(n):
        score += estimate_cost(i)
    return polish_score(score)

def estimate_cost(value):
    if value % 4 == 0:
        return multiply_cost(value)
    return value + STEP

def multiply_cost(value):
    return value * multiplier

def polish_score(amount):
    while amount > LIMIT:
        amount -= STEP
    return amount

def read_token():
    return token