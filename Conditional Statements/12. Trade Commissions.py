town = input()
volume = float(input())
if town == "Sofia" and (0 <= volume <= 500):
    print(f"{volume * 0.05:.2f}")
elif town == "Sofia" and (500 <= volume <= 1000):
    print(f"{volume * 0.07:.2f}")
elif town == "Sofia" and (1000 <= volume <= 10000):
    print(f"{volume * 0.08:.2f}")
elif town == "Sofia" and (10000 < volume):
    print(f"{volume * 0.12:.2f}")
elif town == "Varna" and (0 <= volume <= 500):
    print(f"{volume * 0.045:.2f}")
elif town == "Varna" and (500 <= volume <= 1000):
    print(f"{volume * 0.075:.2f}")
elif town == "Varna" and (1000 <= volume <= 10000):
    print(f"{volume * 0.10:.2f}")
elif town == "Varna" and (10000 < volume):
    print(f"{volume * 0.13:.2f}")
elif town == "Plovdiv" and (0 <= volume <= 500):
    print(f"{volume * 0.055:.2f}")
elif town == "Plovdiv" and (500 <= volume <= 1000):
    print(f"{volume * 0.08:.2f}")
elif town == "Plovdiv" and (1000 <= volume <= 10000):
    print(f"{volume * 0.12:.2f}")
elif town == "Plovdiv" and (10000 < volume):
    print(f"{volume * 0.145:.2f}")
else:
    print("error")