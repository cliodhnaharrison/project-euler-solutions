"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
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

ans = 0

for i in range(7654321, 1234567, -1):
    print (i)
    p = str(i)
    if "1" in p and "2" in p and "3" in p and "4" in p and "5" in p and "6" in p and "7" in p:
        print (is_prime(i))
        if is_prime(i):
            ans = int(p)
            break

print (ans)
