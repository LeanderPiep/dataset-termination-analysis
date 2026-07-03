threshold = 100
step = 3
start = 1

def main():
    value = start
    while value < threshold:
        value = increment_value(value)
    return value

def increment_value(x):
    return x + step

def get_threshold():
    return threshold