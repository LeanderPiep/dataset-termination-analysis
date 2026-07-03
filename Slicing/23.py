BASE_LEVEL = 6
TOP_LEVEL = 160
STEP = 3
OFFSET = 9
profile = 44

def main(n):
    total = BASE_LEVEL
    for current in range(n):
        total += resolve_value(current)
        if total > TOP_LEVEL:
            total = compress_value(total)
    return total

def resolve_value(item):
    if item % 2 == 0:
        return item + OFFSET
    return item * 2

def compress_value(amount):
    return amount // STEP

def load_profile():
    return profile