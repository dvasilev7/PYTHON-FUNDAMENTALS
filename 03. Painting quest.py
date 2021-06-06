collection_of_numbers = [int(number) for number in input().split()]

command = input()
while not command == "END":
    instructions = command.split()
    if instructions[0] == "Change":
        first_num = int(instructions[1])
        changed_num = int(instructions[2])
        if first_num in collection_of_numbers:
            for num in range(len(collection_of_numbers)):
                if collection_of_numbers[num] == first_num:
                    collection_of_numbers[num] = changed_num
    elif instructions[0] == "Hide":
        painting_num = int(instructions[1])
        if painting_num in collection_of_numbers:
            [collection_of_numbers.remove(num) for num in collection_of_numbers if num == painting_num]
    elif instructions[0] == "Switch":
        f_num = int(instructions[1])
        s_num = int(instructions[2])
        if f_num in collection_of_numbers and s_num in collection_of_numbers:
            for num in range(len(collection_of_numbers)):
                if collection_of_numbers[num] == f_num:
                    a = num
                elif collection_of_numbers[num] == s_num:
                    b = num
            collection_of_numbers[a], collection_of_numbers[b] = collection_of_numbers[b], collection_of_numbers[a]
    elif instructions[0] == "Insert":
        index = int(instructions[1]) + 1
        element = int(instructions[2])
        if index < len(collection_of_numbers):
            collection_of_numbers.insert(index, element)
    elif instructions[0] == "Reverse":
        collection_of_numbers.reverse()
    command = input()

for_print = [str(num)for num in collection_of_numbers]

print(" ".join(for_print))