biscuits = input().split(", ")

command = input()
while not command == "Eat":
    action = command.split()
    if action[0] == "Update-Any":
        for i in range(len(biscuits)):
            if biscuits[i] == action[1]:
                biscuits[i] = "Out of stock"
    if action[0] == "Remove":
        bis = action[1]
        index = int(action[2])
        if index < len(biscuits):
            biscuits[index] = bis
    if action[0] == "Update-Last":
        biscuits[-1] = action[1]
    if action[0] == "Rearrange":
        for biscuit in biscuits:
            if action[1] == biscuit:
                biscuits.remove(action[1])
                biscuits.append(action[1])
    command = input()

collection = [biscuit for biscuit in biscuits if biscuit != "Out of stock"]
print(" ".join(collection))
