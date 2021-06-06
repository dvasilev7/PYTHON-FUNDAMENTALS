raw_key = input()
action = input()
while not action == "Generate":
    action_list = action.split(">>>")
    if action_list[0] == "Contains":
        if action_list[1] in raw_key:
            print(f"{raw_key} contains {action_list[1]}")
        else:
            print(f"Substring not found!")
    elif action_list[0] == "Flip":
        start_i = int(action_list[2])
        final_i = int(action_list[3])
        to_change = ""
        if action_list[1] == "Upper":
            for index in range(start_i, final_i):
                to_change += raw_key[index]
            upper = to_change.upper()
            raw_key = raw_key.replace(f"{to_change}", f"{upper}", 1)
        elif action_list[1] == "Lower":
            for index in range(start_i, final_i):
                to_change += raw_key[index]
            lower = to_change.lower()
            raw_key = raw_key.replace(f"{to_change}", f"{lower}", 1)
        print(f"{raw_key}")
    elif action_list[0] == "Slice":
        start_i = int(action_list[1])
        final_i = int(action_list[2])
        to_remove = ""
        for index in range(start_i, final_i):
            to_remove += raw_key[index]
        raw_key = raw_key.replace(to_remove, "", 1)
        print(f"{raw_key}")
    action = input()

print(f"Your activation key is: {raw_key}")
