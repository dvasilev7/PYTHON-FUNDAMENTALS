n = int(input())
current = 1
current_is_bigger_than_n = False

for row in range(1, n + 1):
    for col in range(1, row + 1):
        print(f"{str(current)}", end = ' ')
        current += 1
        if current > n:
            current_is_bigger_than_n = True
            break
    if current_is_bigger_than_n:
        break
    print()
