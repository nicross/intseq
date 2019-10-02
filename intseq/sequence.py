import math
from collections import deque
from .utility import cached_pure_generator
from .utility import digit_product
from .utility import digit_sum
from .utility import is_prime
from .utility import is_square
from .utility import prime_factorization
from .utility import yield_prime

# The zero sequence
def A000004():
    while True:
        yield 0

# The one sequence
def A000012():
    while True:
        yield 1

# The positive integers
def A000027():
    n = 1
    while True:
        yield n
        n += 1

# Parity of n
def A000035():
    while True:
        yield 0
        yield 1

# The primes
def A000040():
    for n in yield_prime():
        yield n

# Mersenne exponents
@cached_pure_generator
def A000043():
    n = 2
    while True:
        if is_prime(n) and is_prime(2 ** n - 1):
            yield n
        n += 1

# Fibonacci numbers
def A000045():
    [previous, current] = [0, 1]

    yield previous
    yield current

    while True:
        [previous, current] = [current, current + previous]
        yield current

# Powers of 2
def A000079():
    n = 0
    while True:
        yield 2 ** n
        n += 1

# Catalan numbers
def A000108():
    n = 0
    while True:
        x = math.factorial(2 * n)
        x /= math.factorial(n + 1) * math.factorial(n)
        yield int(x)
        n += 1

# The squares
def A000290():
    n = 0
    while True:
        yield n ** 2
        n += 1

# Mersenne primes
@cached_pure_generator
def A000668():
    n = 2
    while True:
        if is_prime(n):
            x = 2 ** n - 1

            if is_prime(x):
                yield x

        n += 1

# Golomb's sequence
def A001462():
    for n in [1, 2, 2]:
        yield n

    q = deque([2])
    n = 3

    while True:
        for i in range(q[0]):
            yield n
            q.append(n)

        n += 1
        q.popleft()

# n appears n times
def A002024():
    n = 1
    while True:
        for x in range(n):
            yield n
        n += 1

# The odd numbers
def A005408():
    n = 1
    while True:
        yield n
        n += 2

# The nonnegative even numbers
def A005843():
    n = 0
    while True:
        yield n
        n += 2

# Greatest prime factorization of n
def A006530():
    yield 1
    n = 2
    while True:
        yield prime_factorization(n)[-1]
        n += 1

# Digital sum of n
def A007953():
    n = 0
    while True:
        yield digit_sum(n)
        n += 1

# Product of decimal digits of n
def A007954():
    n = 0
    while True:
        yield digit_product(n)
        n += 1
