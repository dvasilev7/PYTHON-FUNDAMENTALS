items = input()
budget = float(input())
items_list = items.split("|")
profit = 0
new_price_list = []
for item in items_list:
    item_type, price = item.split("->")
    price = float(price)
    if item_type == "Clothes" and price > 50.00:
        continue
    elif item_type == "Shoes" and price > 35.00:
        continue
    elif item_type == "Accessories" and price > 20.50:
        continue
    if budget >= price:
        budget -= price
        item_profit = price * 0.40
        profit += item_profit
        new_price = price + item_profit
        new_price_list.append(new_price)
for fire_price in new_price_list:
    print(f"{fire_price:.2f}", end=" ")
print()
print(f"Profit: {profit:.2f}")
if sum(new_price_list) + budget >= 150:
    print("Hello, France!")
else:
    print("Time to go.")