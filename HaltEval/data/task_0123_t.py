def f(x):
    count = 0
    a = x
    while a > 1:
        tmp = a % 2
        if tmp == 0:
            a = a // 2
        else:
            a = a - 1
        count += 1
    return count