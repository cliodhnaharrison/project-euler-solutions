"""
The sum of the squares of the first ten natural numbers is: 385
The square of the sum of the first ten natural numbers is: 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

nat_num_sum = sum([x for x in range(1,101)])
nat_num_sq_sum = sum([x**2 for x in range(1,101)])

ans = (nat_num_sum**2) - nat_num_sq_sum
print (ans)
