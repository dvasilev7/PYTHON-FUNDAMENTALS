n1 = int(input())
n2 = int(input())
operator = input()
result = ""
if operator == "+":
    if (n1 + n2) % 2 == 0:
        result = "even"
    else:
        result = "odd"
    print(f"{n1} {operator} {n2} = {n1 + n2} - {result}")
if operator == "-":
    if (n1 - n2) % 2 == 0:
        result = "even"
    else:
        result = "odd"
    print(f"{n1} {operator} {n2} = {n1 - n2} - {result}")
if operator == "*":
    if (n1 * n2) % 2 == 0:
        result = "even"
    else:
        result = "odd"
    print(f"{n1} {operator} {n2} = {n1 * n2} - {result}")
if operator == "/":
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")
    else:
        print(f"{n1} / {n2} = {n1 / n2:.2f}")
if operator == "%":
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")
    else:
        print(f"{n1} % {n2} = {n1 % n2}")