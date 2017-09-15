"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


ans = 0

for i in range(999, 100, -1):
    for j in range(999, 100, -1):
        print (i*j)
        p = str(i*j)
        if p[0] == p[-1] and p[1] == p[-2] and p[2] == p[-3]:
            if i*j > ans:
                ans = i*j


print (ans)
