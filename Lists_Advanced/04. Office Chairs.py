n_rooms = int(input())
free_chairs = 0
chairs_are_enough = True

for room_num in range(1, n_rooms + 1):
    chairs, people = input().split()
    people = int(people)
    chairs_list = [int(1) for x in chairs]
    count_of_chairs = sum(chairs_list)
    difference = abs(count_of_chairs - people)
    if count_of_chairs > people:
        free_chairs += difference
    elif count_of_chairs < people:
        print(f"{difference} more chairs needed in room {room_num}")
        chairs_are_enough = False

if chairs_are_enough:
    print(f"Game On, {free_chairs} free chairs left")
