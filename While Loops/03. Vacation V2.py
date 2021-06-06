needed_money = float(input())
money_in_hand = float(input())
spending_days = 0
total_days = 0
while True:
    action = input()
    current_sum = float(input())
    total_days += 1
    if action == "spend":
        money_in_hand -= current_sum
        spending_days += 1
        if money_in_hand <= 0:
            money_in_hand = 0
        if spending_days == 5:
            break
    elif action == "save":
        money_in_hand += current_sum
        if money_in_hand >= needed_money:
            break
        spending_days = 0

if money_in_hand >= needed_money:
    print(f"You saved the money for {total_days} days.")
else:
    print("You can't save the money.")
    print(total_days)