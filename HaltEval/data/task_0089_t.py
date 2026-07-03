def f(x, M):
    if M > 0:
        while x != M:
            if x > M:
                x = 0
            else:
                x = x + 1
    return None