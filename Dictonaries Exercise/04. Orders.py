def multiplyList(myList):
    result = 1
    for x in myList:
        result = result * x
    return result


command = input()
prod_dict = {}

while command != "buy":
    name, price, quantity = command.split()
    price = float(price)
    quantity = int(quantity)
    if name not in prod_dict:
        prod_dict[name] = []
        prod_dict[name].append(price)
        prod_dict[name].append(quantity)
    else:
        list = prod_dict[name]
        list[0] = price
        list[1] += quantity
    command = input()

for key, value in prod_dict.items():
    result = multiplyList(value)
    print(f"{key} -> {result:.2f}")