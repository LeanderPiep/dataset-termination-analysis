def f(x, y):
    while y != 0:
        tmp = y
        xtmp = x
        
        if x <= 0 or y <= 0:
            y = 0
        else:
            if x == y:
                y = 0
            else:
                while xtmp > y:
                    xtmp = xtmp - y
        
        y = xtmp
        x = tmp
    
    return None