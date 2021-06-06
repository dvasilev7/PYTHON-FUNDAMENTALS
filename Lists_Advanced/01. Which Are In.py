string_1 = input().split(", ")
string_2 = input().split(", ")
substrings = []
[substrings.append(string) for string in string_1 for el in string_2 if string in el if string not in substrings]

print(substrings)
