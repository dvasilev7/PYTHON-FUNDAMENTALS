targets = [int(target) for target in input().split()]
targets_shot = 0

command = input()
while not command == "End":
    index = int(command)
    if index <= len(targets) - 1:
        initial_value = targets[index]
        if targets[index] != -1:
            targets[index] = -1
            targets_shot += 1
        for target in range(len(targets)):
            if targets[target] <= initial_value and targets[target] != -1:
                targets[target] += initial_value
            elif targets[target] > initial_value and targets[target] != -1:
                targets[target] -= initial_value
    command = input()
else:
    targets_final = [str(target) for target in targets]
    print(f"Shot targets: {targets_shot} -> {' '.join(targets_final)}")