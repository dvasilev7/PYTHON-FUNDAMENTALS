from math import fabs
width = int(input())
length = int(input())
height = int(input())
space = width * length * height

command = input()
while command != "Done":
    boxes = int(command)
    free_space = space - boxes
    if free_space <= 0:
        print(f"No more free space! You need {fabs(free_space)} Cubic meters more.")
        break
    command = input()
else:
    print(f"{free_space} Cubic meters left.")




