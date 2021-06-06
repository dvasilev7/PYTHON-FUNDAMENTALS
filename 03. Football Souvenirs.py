team = input()
souvenir = input()
count_souvenirs = int(input())
flags = 0
caps = 0
posters = 0
stickers = 0
souvenir_total_price = 0
if team == "Argentina":
    flags = 3.25
    caps = 7.20
    posters = 5.10
    stickers = 1.25
    if souvenir == "flags":
        souvenir_total_price = count_souvenirs * flags
        print(f"Pepi bought {count_souvenirs} {souvenir} of {team} for {souvenir_total_price:.2f} lv.")
    elif souvenir == "caps":
        souvenir_total_price = count_souvenirs * caps
        print(f"Pepi bought {count_souvenirs} {souvenir} of {team} for {souvenir_total_price:.2f} lv.")
    elif souvenir == "posters":
        souvenir_total_price = count_souvenirs * posters
        print(f"Pepi bought {count_souvenirs} {souvenir} of {team} for {souvenir_total_price:.2f} lv.")
    elif souvenir == "stickers":
        souvenir_total_price = count_souvenirs * stickers
        print(f"Pepi bought {count_souvenirs} {souvenir} of {team} for {souvenir_total_price:.2f} lv.")
    else:
        print("Invalid stock!")
elif team == "Brazil":
    flags = 4.20
    caps = 8.50
    posters = 5.35
    stickers = 1.20
    if souvenir == "flags":
        souvenir_total_price = count_souvenirs * flags
        print(f"Pepi bought {count_souvenirs} {souvenir} of {team} for {souvenir_total_price:.2f} lv.")
    elif souvenir == "caps":
        souvenir_total_price = count_souvenirs * caps
        print(f"Pepi bought {count_souvenirs} {souvenir} of {team} for {souvenir_total_price:.2f} lv.")
    elif souvenir == "posters":
        souvenir_total_price = count_souvenirs * posters
        print(f"Pepi bought {count_souvenirs} {souvenir} of {team} for {souvenir_total_price:.2f} lv.")
    elif souvenir == "stickers":
        souvenir_total_price = count_souvenirs * stickers
        print(f"Pepi bought {count_souvenirs} {souvenir} of {team} for {souvenir_total_price:.2f} lv.")
    else:
        print("Invalid stock!")
elif team == "Croatia":
    flags = 2.75
    caps = 6.90
    posters = 4.95
    stickers = 1.10
    if souvenir == "flags":
        souvenir_total_price = count_souvenirs * flags
        print(f"Pepi bought {count_souvenirs} {souvenir} of {team} for {souvenir_total_price:.2f} lv.")
    elif souvenir == "caps":
        souvenir_total_price = count_souvenirs * caps
        print(f"Pepi bought {count_souvenirs} {souvenir} of {team} for {souvenir_total_price:.2f} lv.")
    elif souvenir == "posters":
        souvenir_total_price = count_souvenirs * posters
        print(f"Pepi bought {count_souvenirs} {souvenir} of {team} for {souvenir_total_price:.2f} lv.")
    elif souvenir == "stickers":
        souvenir_total_price = count_souvenirs * stickers
        print(f"Pepi bought {count_souvenirs} {souvenir} of {team} for {souvenir_total_price:.2f} lv.")
    else:
        print("Invalid stock!")
elif team == "Denmark":
    flags = 3.10
    caps = 6.50
    posters = 4.80
    stickers = 0.90
    if souvenir == "flags":
        souvenir_total_price = count_souvenirs * flags
        print(f"Pepi bought {count_souvenirs} {souvenir} of {team} for {souvenir_total_price:.2f} lv.")
    elif souvenir == "caps":
        souvenir_total_price = count_souvenirs * caps
        print(f"Pepi bought {count_souvenirs} {souvenir} of {team} for {souvenir_total_price:.2f} lv.")
    elif souvenir == "posters":
        souvenir_total_price = count_souvenirs * posters
        print(f"Pepi bought {count_souvenirs} {souvenir} of {team} for {souvenir_total_price:.2f} lv.")
    elif souvenir == "stickers":
        souvenir_total_price = count_souvenirs * stickers
        print(f"Pepi bought {count_souvenirs} {souvenir} of {team} for {souvenir_total_price:.2f} lv.")
    else:
        print("Invalid stock!")
else:
    print("Invalid country!")
