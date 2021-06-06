n = int(input())
p1 = 0
p2 = 0
p3 = 0
number_2 = 0
number_3 = 0
number_4 = 0
for numbers in range(1, n + 1):
    p = int(input())
    if p % 2 == 0:
        p1 += 1
        number_2 = p1 / n * 100
    if p % 3 == 0:
        p2 += 1
        number_3 = p2 / n * 100
    if p % 4 == 0:
        p3 += 1
        number_4 = p3 / n * 100
print(f"{number_2:.2f}%")
print(f"{number_3:.2f}%")
print(f"{number_4:.2f}%")