hour = int(input())
day = input()
if day == "Monday" and 18 >= hour >= 10:
    print("open")
elif day == "Tuesday" and 18 >= hour >= 10:
    print("open")
elif day == "Wednesday" and 18 >= hour >= 10:
    print("open")
elif day == "Thursday" and 18 >= hour >= 10:
    print("open")
elif day == "Friday" and 18 >= hour >= 10:
    print("open")
elif day == "Saturday" and 18 >= hour >= 10:
    print("open")
else:
    print("closed")