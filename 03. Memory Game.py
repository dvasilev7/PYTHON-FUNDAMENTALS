elements = [str(element) for element in input().split()]

moves_counter = 0

command = input()
while not command == "end":
    moves_counter += 1
    index1, index2 = command.split()
    first_index = int(index1)
    second_index = int(index2)
    element_1 = elements[first_index]
    element_2 = elements[second_index]
    if 0 <= first_index <= len(elements) and first_index != second_index and 0 <= second_index <= len(elements):
        if element_1 == element_2:
            element = element_1
            if first_index > second_index:
                elements.pop(first_index)
                elements.pop(second_index)
            elif first_index < second_index:
                elements.pop(second_index)
                elements.pop(first_index)
            print(f"Congrats! You have found matching elements - {element}!")
        else:
            print("Try again!")
    else:
        insert_index = int(len(elements) / 2)
        elements.insert(insert_index, f"-{moves_counter}a")
        elements.insert(insert_index, f"-{moves_counter}a")
        print("Invalid input! Adding additional elements to the board")
    if len(elements) == 0 or len(elements) == 1:
        break
    command = input()

if len(elements) > 1:
    print("Sorry you lose :(")
    print(" ".join(elements))
else:
    print(f"You have won in {moves_counter} turns!")