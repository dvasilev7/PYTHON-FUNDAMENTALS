energy = 100
coins = 100
events = input()
events_list = events.split("|")
is_not_bankrupt = True
for iteration in events_list:
    event, value = iteration.split("-")
    value = int(value)
    if event == "rest":
        initial_energy = energy
        energy += value
        if energy > 100:
            energy = 100
        print(f"You gained {energy - initial_energy} energy.")
        print(f"Current energy: {energy}.")
    elif event == "order":
        initial_coins = coins
        if energy - 30 >= 0:
            coins += value
            energy -= 30
            print(f"You earned {coins - initial_coins} coins.")
        else:
            energy += 50
            print("You had to rest!")
    else:
        if coins > value:
            print(f"You bought {event}.")
            coins -= value
        else:
            print(f"Closed! Cannot afford {event}.")
            is_not_bankrupt = False
            break
if is_not_bankrupt:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")