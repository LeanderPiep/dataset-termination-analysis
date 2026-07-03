# label: f

FEATURE_ENABLED = True
MAX_ALLOWED_VALUE = (0x7fffffff * 2 + 1) // 2


def is_valid_input(total_value, divisor):
    if divisor >= MAX_ALLOWED_VALUE:
        return False
    if divisor < 1:
        return False
    if total_value >= MAX_ALLOWED_VALUE:
        return False
    return True


def main(total_value, divisor):
    if not FEATURE_ENABLED:
        return None

    if not is_valid_input(total_value, divisor):
        return None

    quotient = 0
    remainder = total_value
    current_divisor = divisor

    if remainder < current_divisor:
        while total_value == quotient * current_divisor + remainder:
            if 2 * (current_divisor // 2) == current_divisor:
                quotient = 2 * quotient
                current_divisor = current_divisor // 2
                if remainder >= current_divisor:
                    quotient = quotient + 1
                    remainder = remainder - current_divisor

    return None