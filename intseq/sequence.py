import math
from collections import deque
from .utility import is_prime
from .utility import is_square

# The zero sequence
def A000004():
    while True:
        yield 0

# The positive integers
def A000027():
    n = 1
    while True:
        yield n
        n += 1

# The primes
def A000040():
    n = 2
    while True:
        if is_prime(n):
            yield n

        n += 1

# Mersenne exponents
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
