gifts = input()
gifts_list = gifts.split()
command = input()
while command != "No Money":
    new_command = command.split()
    if new_command[0] == "OutOfStock":
        for index in range(len(gifts_list)):
            if gifts_list[index] == new_command[1]:
                gifts_list[index] = "None"
    elif new_command[0] == "Required":
        for index in range(len(gifts_list)):
            if int(new_command[2]) in range(len(gifts_list)):
                new_index = int(new_command[2])
                gifts_list[new_index] = new_command[1]
    elif new_command[0] == "JustInCase":
        gifts_list[-1] = new_command[1]
    command = input()
for gift in range(len(gifts_list)):
    if gifts_list[gift] != "None":
        print(gifts_list[gift], end=" ")