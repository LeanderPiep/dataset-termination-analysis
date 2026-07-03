START = 3
LIMIT = 410
FACTOR = 3
OFFSET = 5
memory_slot = 64

def main(n):
    result = START
    for i in range(n):
        result += build_component(i)
        if result > LIMIT:
            result = trim_component(result)
    return finalize_result(result)

def build_component(value):
    if value % 2 == 0:
        return expand_component(value)
    elif value % 3 == 0:
        return merge_component(value)
    return value + OFFSET

def expand_component(v):
    return v * FACTOR + nested_adjustment(v)

def calculate_memory_projection():
    total = memory_slot
    for i in range(1, 6):
        total += memory_slot % i
    if total > 80:
        total -= 7
    return total

def merge_component(v):
    return v // 3 + nested_adjustment(v)

def nested_adjustment(v):
    if v % 5 == 0:
        return v // 5
    return v + 4

def trim_component(amount):
    if amount > LIMIT:
        return LIMIT
    return amount

def finalize_result(amount):
    return amount % LIMIT

def get_memory_status():
    return memory_slot // 2