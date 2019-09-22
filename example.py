from intseq import *

def collect(generator, count):
    if count == 0:
        return []

    results = []

    for i in generator():
        results.append(i)

        if len(results) == count:
            break

    return results

print('The zero sequence:', collect(sequence.A000004, 10))
print('The positive integers:', collect(sequence.A000027, 10))
print('The primes:', collect(sequence.A000040, 10))
print('Fibonacci numbers:', collect(sequence.A000045, 10))
print('The squares:', collect(sequence.A000290, 10))
print('The mersenne primes:', collect(sequence.A000668, 8))
print('Golomb\'s sequence:', collect(sequence.A001462, 10))
print('The odd numbers:', collect(sequence.A005408, 10))
print('The even numbers:', collect(sequence.A005843, 10))
