"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

from math import sqrt

def is_prime(n):
    prime = True
    i = 2
    while i <= sqrt(n):
        if n % i == 0:
            prime = False
            break
        i += 1
    return prime

primes = []

for i in range(2, 1000000000):
    if len(primes) > 10000:
        break
    else:
        if is_prime(i):
            primes.append(i)

print (primes[10000])
