numbers = input().split(", ")
list_of_numbers = [int(number) for number in numbers]
maximum = max(list_of_numbers)
for tens in range(10, maximum + 10, 10):
    tens_list = []
    [tens_list.append(number) for number in list_of_numbers if number <= tens]
    list_of_numbers = list(filter(lambda number: number > tens, list_of_numbers))
    print(f"Group of {tens}'s: {tens_list}")
