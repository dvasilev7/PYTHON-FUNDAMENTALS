needed_money = float(input())
money_in_hand = float(input())
spending_days = 0
total_days = 0

while money_in_hand < needed_money and spending_days < 5:
    action = input()
    current_money = float(input())
    total_days += 1
    if action == "save":
        money_in_hand += current_money
        spending_days = 0
    if action == "spend":
        money_in_hand -= current_money
        spending_days += 1
        if money_in_hand < 0:
            money_in_hand = 0
if money_in_hand >= needed_money:
    print(f"You saved the money for {total_days} days.")
else:
    print("You can't save the money.")
    print(total_days)
