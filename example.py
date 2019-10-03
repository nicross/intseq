from intseq import *

def collect(generator, count):
    if count <= 0:
        return []

    results = []

    for n in generator():
        results.append(n)

        if len(results) == count:
            break

    return results

def get(generator, index):
    i = 0
    for n in generator():
        if i == index:
            return n
        i += 1

print('The zero sequence:', collect(sequence.A000004, 10))
print('The one sequence:', collect(sequence.A000012, 10))
print('The positive integers:', collect(sequence.A000027, 10))
print('Parity of n:', collect(sequence.A000035, 10))
print('The primes:', collect(sequence.A000040, 10))
print('Mersenne exponents:', collect(sequence.A000043, 8))
print('Fibonacci numbers:', collect(sequence.A000045, 10))
print('Powers of 2:', collect(sequence.A000079, 10))
print('Catalan numbers:', collect(sequence.A000108, 10))
print('The squares:', collect(sequence.A000290, 10))
print('Mersenne primes:', collect(sequence.A000668, 8))
print('Golomb\'s sequence:', collect(sequence.A001462, 10))
print('n appears n times:', collect(sequence.A002024, 10))
print('The odd numbers:', collect(sequence.A005408, 10))
print('The even numbers:', collect(sequence.A005843, 10))
print('Greatest prime factor of n:', collect(sequence.A006530, 10))
print('Digital sum of n:', collect(sequence.A007953, 10))
print('Digital product of n:', collect(sequence.A007954, 10))
print('Characteristic function of primes:', collect(sequence.A010051, 10))
print('Hoax numbers:', collect(sequence.A019506, 10))
