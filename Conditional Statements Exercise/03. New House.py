from math import fabs
type_flowers = input()
number_flowers = int(input())
budget = int(input())
price = 0

if type_flowers == "Roses":
    price = 5
    if number_flowers > 80:
        price *= 0.9
if type_flowers == "Dahlias":
    price = 3.80
    if number_flowers > 90:
        price *= 0.85
if type_flowers == "Tulips":
    price = 2.80
    if number_flowers > 80:
        price *= 0.85
if type_flowers == "Narcissus":
    price = 3
    if number_flowers < 120:
        price *= 1.15
if type_flowers == "Gladiolus":
    price = 2.50
    if number_flowers < 80:
        price *= 1.20
if budget - price * number_flowers >= 0:
    print(f"Hey, you have a great garden with {number_flowers} {type_flowers} and {budget - price * number_flowers:.2f} leva left.")
if budget - price * number_flowers < 0:
    print(f"Not enough money, you need {fabs(budget - price * number_flowers):.2f} leva more.")