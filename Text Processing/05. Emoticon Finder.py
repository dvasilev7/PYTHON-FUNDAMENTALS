string = input()
for symbol in range(0, len(string), 1):
    if string[symbol] == ":" and string[symbol + 1] != " ":
        print(f"{string[symbol]}{string[symbol + 1]}")
