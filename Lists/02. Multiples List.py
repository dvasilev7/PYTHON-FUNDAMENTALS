factor = int(input())
count = int(input())
list_numbers = [factor]
new_factor = factor
for i in range(count - 1):
    new_factor += factor
    list_numbers.append(new_factor)
print(list_numbers)

