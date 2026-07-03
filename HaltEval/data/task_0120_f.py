def f(x):
    while x != 0:
        if -5 <= x <= 35:
            if x < 0:
                x = -5
            else:
                if x > 30:
                    x = 35
                else:
                    x = x - 1
        else:
            x = 0
    return None