from sys import maxsize

numbers = input()
count_if_removed = int(input())
numbers_list = numbers.split()
new_numbers_list = []
for n in range(len(numbers_list)):
    number = int(numbers_list[n])
    new_numbers_list.append(number)
numbers_list = new_numbers_list
# research for a way to use map
for i in range(count_if_removed):
    minimum = maxsize
    for num in range(len(numbers_list)):
        if numbers_list[num] < minimum:
            minimum = int(numbers_list[num])
    numbers_list.remove(minimum)
print(numbers_list)