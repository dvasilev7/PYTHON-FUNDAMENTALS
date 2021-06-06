from math import fabs
cake_width = int(input())
cake_len = int(input())
cake_size = cake_width * cake_len
command = input()
while command != "STOP":
    pieces = int(command)
    cake_size -= pieces
    if cake_size <= 0:
        print(f"No more cake left! You need {int(fabs(cake_size))} pieces more.")
        break
    command = input()
else:
    print(f"{cake_size} pieces are left.")
