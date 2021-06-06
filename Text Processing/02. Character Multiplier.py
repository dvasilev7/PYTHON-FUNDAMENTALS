str1, str2 = input().split(" ")
total = 0

if len(str1) > len(str2):
    for letter in range(len(str2)):
        total += ord(str2[letter]) * ord(str1[letter])
    n = len(str1) - len(str2)
    for letter in range(-1, -n - 1, -1):
        total += ord(str1[letter])
elif len(str2) > len(str1):
    for letter in range(len(str1)):
        total += ord(str1[letter]) * ord(str2[letter])
    n = len(str2) - len(str1)
    for letter in range(-1, -n - 1, -1):
        total += ord(str2[letter])
else:
    for letter in range(len(str1)):
        total += ord(str1[letter]) * ord(str2[letter])

print(total)