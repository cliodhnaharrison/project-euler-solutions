ans = 0

for c in range(1,500):
    for b in range(1, 500):
        for a in range(1, 500):
            if a + b + c == 1000:
                if (a**2) + (b**2) == (c**2):
                    ans = a * b * c
                    break

print (ans)
