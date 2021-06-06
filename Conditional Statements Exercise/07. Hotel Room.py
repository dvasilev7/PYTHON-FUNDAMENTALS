month = input()
count_of_nights = int(input())
studio = 0
apartment = 0
#May, June, July, August, September или October
if month == "May" or month == "October":
    studio = 50
    apartment = 65
    if 14 >= count_of_nights > 7:
        studio *= 0.95
    if count_of_nights > 14:
        studio *= 0.70
        apartment *= 0.90
if month == "June" or month == "September":
    studio = 75.20
    apartment = 68.70
    if count_of_nights > 14:
        studio *= 0.80
        apartment *= 0.90
if month == "August" or month == "July":
    studio = 76
    apartment = 77
    if count_of_nights > 14:
        apartment *= 0.90
print(f"Apartment: {count_of_nights * apartment:.2f} lv.")
print(f"Studio: {count_of_nights * studio:.2f} lv.")

