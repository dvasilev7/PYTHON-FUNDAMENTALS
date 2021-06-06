symbols = {}

text = input()
for symbol in text:
    if symbol != " ":
        if symbol not in symbols:
            symbols[symbol] = 1
        else:
            symbols[symbol] += 1
    else:
        pass

for key, value in symbols.items():
    print(f"{key} -> {value}")
