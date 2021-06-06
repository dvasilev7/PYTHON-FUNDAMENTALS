usernames = input().split(", ")
isValid = True
valid_usernames = []

for username in range(len(usernames)):
    isValid = True
    if 3 > len(usernames[username]) or len(usernames[username]) > 16:
        isValid = False
    for symbol in usernames[username]:
        if symbol.isnumeric() == False and symbol.isalpha() == False and symbol != "-" and symbol != "_":
            isValid = False
    if isValid:
        valid_usernames.append(usernames[username])

print("\n".join(valid_usernames))
