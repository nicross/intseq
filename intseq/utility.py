import math
import operator

from functools import reduce

def cached_pure_function(fn):
    cache = {}

    def wrapper(*args):
        if args in cache:
            return cache[args]

        x = fn(*args)
        cache[args] = x

        return x

    return wrapper

def cached_pure_generator(fn):
    caches = {}
    iterator = fn()

    def wrapper(*args):
        index = 0

        if args not in caches:
            caches[args] = []

        cache = caches[args]

        while True:
            if index < len(cache):
                n = cache[index]
            else:
                n = next(iterator)
                cache.append(n)

            yield n
            index += 1

    return wrapper

def digit_product(n):
    return reduce(operator.mul, [digit for digit in digits(n)])

def digit_sum(n):
    return reduce(operator.add, [digit for digit in digits(n)])

def digits(n):
    for digit in str(n):
        yield int(digit)

@cached_pure_function
def is_prime(n):
    if n <= 1:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    # IDEA: Would checking only for prime factors be an optimization here?
    # TODO: Leverage yield_prime() recursively or cache known primes
    # SEE: https://en.wikipedia.org/wiki/Fundamental_theorem_of_arithmetic
    for i in range(3, math.ceil(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False

    return True

def is_coprime(a, b):
    a = prime_factorization(a)
    b = prime_factorization(b)

    for n in a:
        if n in b:
            return False
    return True

def is_square(n):
    sqrt = math.sqrt(n)
    return sqrt == math.floor(sqrt)

def prime_factorization(n, multiplicity = False):
    if n <= 1:
        return []

    if is_prime(n):
        return [n]

    result = []

    for i in yield_prime():
        appended = False

        while n % i == 0:
            if multiplicity or not appended:
                result.append(i)
                appended = True

            n /= i

        if n == 1:
            return result

def yield_prime():
    n = 2
    while True:
        if is_prime(n):
            yield n

        n += 1
