RANGE_HIGH = range(81, 126)
RANGE_MEDIUM = range(51, 81)
RANGE_LOW = range(1, 51)

effort = 0
fire_put_out = []

cells = input()
water_amount = int(input())
fire_data = cells.split("#")

for fire in fire_data:
    type_of_fire, value = fire.split(" = ")
    value = int(value)
#   TODO CHECK IF VALUE IS NOT IN TYPE RANGE
    if type_of_fire == "High" and value not in RANGE_HIGH:
        continue
    elif type_of_fire == "Medium" and value not in RANGE_MEDIUM:
        continue
    elif type_of_fire == "Low" and value not in RANGE_LOW:
        continue
#   TODO CHECK IF WATER IS ENOUGH
    if water_amount >= value:
        water_amount -= value
        effort += value * 0.25
        fire_put_out.append(value)
# TODO PRINTOUT DATA FOR PUT OUT FIRE CELLS
print("Cells:")
for fire_value in fire_put_out:
    print(f" - {fire_value}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {sum(fire_put_out)}")
