"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
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

for i in range(2, 2000000):
    if is_prime(i):
        primes.append(i)

print (sum(primes))
