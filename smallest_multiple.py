"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

i = 2521
div = False

while div == False:
    for j in range(1,21):
        if i % j == 0:
            div = True
        else:
            div = False
            break
    i += 1

print (i-1)
