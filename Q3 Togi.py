divisible = 0


for a in range(1,7):
    for b in range(1,7):
        for c in range(1,7):
            for d in range(1,7):
                for e in range(1,7):
                    if a == 2:
                        if b == 5 or c == 5 or d == 5 or e == 5:
                            divisible += 1
                    elif b == 2:
                        if a == 5 or c == 5 or d == 5 or e == 5:
                            divisible += 1
                    elif c == 2:
                        if a == 5 or b == 5 or d == 5 or e == 5:
                            divisible += 1
                    elif d == 2:
                        if a == 5 or c == 5 or b == 5 or e == 5:
                            divisible += 1
                    elif e == 2:
                        if a == 5 or c == 5 or d == 5 or b == 5:
                            divisible += 1

probability = (divisible / 6**5)
print(probability)