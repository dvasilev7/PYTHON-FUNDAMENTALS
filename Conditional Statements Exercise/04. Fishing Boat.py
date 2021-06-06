from math import fabs
budget = int(input())
season = input()
number_of_fisherman = int(input())
price = 0
if season == "Spring":
    price = 3000
elif season == "Summer":
    price = 4200
elif season == "Autumn":
    price = 4200
elif season == "Winter":
    price = 2600
if number_of_fisherman <= 6:
    price *= 0.9
elif 6 < number_of_fisherman <= 11:
    price *= 0.85
else:
    price *= 0.75
if number_of_fisherman % 2 == 0 and season != "Autumn":
    price *= 0.95
if budget - price >= 0:
    print(f"Yes! You have {budget - price:.2f} leva left.")
if budget - price < 0:
    print(f"Not enough money! You need {fabs(budget - price):.2f} leva.")