#directory = input()
#n = 0
#a = 0
#for symbol in range(0, len(directory), 1):
#    if directory[symbol] == ".":
#        n = symbol
#    elif directory[symbol] == "\\":
#        a = symbol

#extension = ""
#for symbol in range(n + 1, len(directory), 1):
#    extension += directory[symbol]
#file_name = ""
#for symbol in range(a + 1, n, 1):
#    file_name += directory[symbol]

#print(f"File name: {file_name}")
#print(f"File extension: {extension}")

directory = input().split("\\")
stop = 0
list = directory[-1]
for symbol in range(1, len(directory[-1]), 1):
    if list[symbol] == ".":
        stop = symbol

extension = list[stop + 1:]
file_name = list[:stop]
print(f"File name: {file_name}")
print(f"File extension: {extension}")
