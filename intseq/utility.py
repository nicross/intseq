import math
import operator

from functools import reduce

def digit_product(n):
    return reduce(operator.mul, [digit for digit in digits(n)])

def digit_sum(n):
    return reduce(operator.add, [digit for digit in digits(n)])

def digits(n):
    for digit in str(n):
        yield int(digit)

def is_prime(n):
    if n == 1:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    for i in range(3, math.ceil(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False

    return True

def is_square(n):
    sqrt = math.sqrt(n)
    return sqrt == math.floor(sqrt)
