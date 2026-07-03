THRESHOLD = 60
OFFSET = 4
MULTIPLIER = 2
cache_entry = 27

def main(n):
    score = 0
    for i in range(n):
        if i % 2 == 0:
            score += build_even_score(i)
        else:
            score += build_odd_score(i)
    if score > THRESHOLD:
        return THRESHOLD
    return score

def build_even_score(value):
    return value * MULTIPLIER

def load_cache_entry():
    total = cache_entry
    total += 3
    return total

def build_odd_score(value):
    return value + OFFSET