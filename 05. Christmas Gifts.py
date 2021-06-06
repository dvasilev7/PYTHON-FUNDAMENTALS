adults_count = 0
kids_count = 0
command = input()
while command != "Christmas":
    age = int(command)
    if age <= 16:
        kids_count += 1
    elif age > 16:
        adults_count += 1
    command = input()
print(f"Number of adults: {adults_count}")
print(f"Number of kids: {kids_count}")
print(f"Money for toys: {kids_count * 5}")
print(f"Money for sweaters: {adults_count * 15}")


