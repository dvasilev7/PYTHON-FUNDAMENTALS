string = input()
for symbol in string:
    if symbol * 2 in string:
        string = string.replace(symbol * 2, symbol)

print(string)
