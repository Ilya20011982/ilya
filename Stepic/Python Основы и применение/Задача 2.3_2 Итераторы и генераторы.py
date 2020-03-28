import itertools


def isprime(num):
    for x in range(2, num):
        if num % x == 0:
            return False
    return True

def primes():
    num = 1
    while True:
        num += 1
        if num == 2:
            yield num
        if num % 2 == 0:
            continue
        if isprime(num):
            yield num


print(list(itertools.takewhile(lambda x: x <= 31, primes())))   # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]