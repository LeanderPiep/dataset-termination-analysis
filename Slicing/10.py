THRESHOLD = 80
STEP_SIZE = 4
BASE_VALUE = 2
reserve = 15

def main(n):
    score = BASE_VALUE
    for current in range(n):
        score += update_score(current)
    while score < THRESHOLD:
        score = raise_score(score)
    return score

def update_score(value):
    if value % 2 == 0:
        return value + STEP_SIZE
    return value // 2

def raise_score(amount):
    return amount + STEP_SIZE

def load_reserve():
    return reserve