BASE = 4
LIMIT = 720
STEP = 5
BONUS = 9
state_value = 105

def main(n):
    total = BASE
    for i in range(n):
        if i % 2 == 0:
            total += compute_primary_branch(i)
        else:
            total += compute_secondary_branch(i)
        if total > LIMIT:
            total = compress_total(total)
    return total

def compute_primary_branch(x):
    return x + BONUS + helper_primary(x)

def load_state_metadata():
    temp = state_value
    values = []
    for i in range(5):
        values.append(temp % (i + 2))
    return sum(values)

def compute_secondary_branch(x):
    if x % 3 == 0:
        return x // 3 + helper_secondary(x)
    return x * 2 + helper_secondary(x)

def helper_primary(v):
    if v % 5 == 0:
        return v // 5
    return v + 2

def helper_secondary(v):
    if v % 7 == 0:
        return v // 7
    return v + 1

def compress_total(amount):
    return amount % LIMIT

def describe_state_bucket():
    if state_value > 100:
        return "priority"
    return "standard"