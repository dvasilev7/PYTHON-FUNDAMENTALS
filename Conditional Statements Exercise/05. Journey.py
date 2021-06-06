budget = float(input())
season = input()
spending = 0
place = ""
destination = ""
if budget <= 100:
    if season == "winter":
        spending = 0.7 * budget
        place = "Hotel"
    elif season == "summer":
        spending = 0.3 * budget
        place = "Camp"
    destination = "Bulgaria"
elif 100 < budget <= 1000:
    if season == "winter":
        spending = 0.8 * budget
        place = "Hotel"
    elif season == "summer":
        spending = 0.4 * budget
        place = "Camp"
    destination = "Balkans"
else:
    destination = "Europe"
    spending = 0.9 * budget
    place = "Hotel"
print(f"Somewhere in {destination}")
print(f"{place} - {spending:.2f}")
