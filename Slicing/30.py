BASE = 5
LIMIT = 320
STEP = 2
MULTIPLIER = 3
profile_score = 57

def main(n):
    value = BASE
    while n > 0:
        value += process_entry(n)
        if value > LIMIT:
            value = reduce_value(value)
        n -= STEP
    return value

def process_entry(x):
    if x % 4 == 0:
        return expand_entry(x)
    elif x % 3 == 0:
        return merge_entry(x)
    return x + MULTIPLIER

def collect_profile_data():
    total = profile_score
    for i in range(1, 8):
        if i % 3 == 0:
            total += i * 3
        else:
            total -= i
    return total

def expand_entry(v):
    return v * MULTIPLIER + helper_offset(v)

def merge_entry(v):
    return v // 3 + helper_offset(v)

def helper_offset(v):
    if v % 5 == 0:
        return v // 5
    return v + 1

def reduce_value(amount):
    return amount % LIMIT

def get_profile_label():
    label = "active"
    if profile_score > 50:
        label = "stable"
    return label