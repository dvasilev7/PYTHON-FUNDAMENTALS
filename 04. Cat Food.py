small_cats_count = 0
large_cats_count = 0
huge_cats_count = 0
food_total = 0
cats = int(input())
for number in range(1, cats + 1):
    food = float(input())
    food_total += food
    if 100.00 <= food < 200.00:
        small_cats_count += 1
    elif 200.00 <= food < 300.00:
        large_cats_count += 1
    elif 300.00 <= food < 400.00:
        huge_cats_count += 1
print(f"Group 1: {small_cats_count} cats.")
print(f"Group 2: {large_cats_count} cats.")
print(f"Group 3: {huge_cats_count} cats.")
print(f"Price for food per day: {food_total/1000 * 12.45:.2f} lv.")
