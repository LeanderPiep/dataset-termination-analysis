def with_defaults(a: str, b: float, c: int, d: bool, e: list, f: Optional[int], g):
    return a + b + c

def outer(a):
    b = a + 1

    def inner(c):
        return b + c

    return inner(b)




