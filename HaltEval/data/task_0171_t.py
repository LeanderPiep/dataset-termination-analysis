
def f(q, a, b):
    while q > 0:
        q = q + a - 1
        olda = a
        a = 3 * olda - 4 * b
        b = 4 * olda + 3 * b
    return 0
