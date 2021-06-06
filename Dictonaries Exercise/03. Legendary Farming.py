materials = input().split()

epic_item_obtained = False
needed_materials_dict = {}
not_needed_materials_dict = {}

needed_materials_dict["motes"] = 0
needed_materials_dict["shards"] = 0
needed_materials_dict["fragments"] = 0
while len(materials) > 0:
    for index in range(1, len(materials), 2):
        material = materials[index]
        material = material.lower()
        value = int(materials[index - 1])
        if material == "motes":
            needed_materials_dict[material] += value
            if needed_materials_dict[material] >= 250:
                print("Dragonwrath obtained!")
                needed_materials_dict[material] -= 250
                epic_item_obtained = True
                break
        elif material == "shards":
            needed_materials_dict[material] += value
            if needed_materials_dict[material] >= 250:
                print("Shadowmourne obtained!")
                needed_materials_dict[material] -= 250
                epic_item_obtained = True
                break
        elif material == "fragments":
            needed_materials_dict[material] += value
            if needed_materials_dict[material] >= 250:
                print("Valanyr obtained!")
                needed_materials_dict[material] -= 250
                epic_item_obtained = True
                break
        else:
            if material in not_needed_materials_dict:
                not_needed_materials_dict[material] += value
            else:
                not_needed_materials_dict[material] = value
    if epic_item_obtained:
        break
    materials = input().split()

scored = {}
for k, v in needed_materials_dict.items():
    if v not in scored:
        scored[v] = []
    scored[v].append(k)

for k in sorted(scored, reverse=True):
    for v in sorted(scored[k]):
        print("{}: {}".format(v, k))

not_needed_materials_dict = dict(sorted(not_needed_materials_dict.items(), key= lambda x: x[0]))
for k, v in not_needed_materials_dict.items():
    print("{}: {}".format(k, v))
