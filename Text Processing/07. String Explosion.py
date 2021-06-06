string = input()
strength_left = 0
trigger = ">"

symbol = 0
while symbol < len(string) - 1:
    to_remove = ""
    if string[symbol] == trigger:
        start = symbol + 1
        strength = int(string[symbol + 1]) + strength_left
        end = start + strength
        for s in range(start, end, 1):
            if string[s] != trigger:
                to_remove += string[s]
            else:
                strength_left = end - s
                break
            if s != len(string) - 1:
                continue
            break
        string = string.replace(to_remove, "", 1)
        symbol = start
    else:
        symbol += 1
print(string)
