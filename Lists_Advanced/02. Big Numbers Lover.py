string = input().split()
reversed_list = string[::-1]
[print(int(num), end="") for num in reversed_list]