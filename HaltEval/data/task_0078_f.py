def f(x, nondet_int):
    if x > nondet_int:
        while x != 0:
            x = x - 1
    return None