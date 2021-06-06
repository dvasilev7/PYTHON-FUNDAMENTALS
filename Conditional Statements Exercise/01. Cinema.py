type = input()
r = int(input())
c = int(input())

price = 0
count = r * c
if type == "Normal":
    price = 7.50
if type == "Premiere":
    price = 12
if type == "Discount":
    price = 5
print(f"{count * price:.2f} leva")