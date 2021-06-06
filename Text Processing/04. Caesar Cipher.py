string = input()
encrypted_string = ""
for symbol in range(0, len(string), 1):
    day = chr(ord(string[symbol]) + 3)
    encrypted_string += day
print(encrypted_string)