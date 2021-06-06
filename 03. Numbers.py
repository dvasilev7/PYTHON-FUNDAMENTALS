numbers = [int(number) for number in input().split()]
average_of_numbers = sum(numbers) / len(numbers)

top_5 = []
[top_5.append(number) for number in numbers if number > average_of_numbers]
top_5.sort(reverse=True)
for number in range(1, len(top_5) + 1):
    if len(top_5) > 5:
        top_5.pop()

sorted_list = (str(number) for number in top_5)
if len(top_5) > 0:
    print(" ".join(sorted_list))
else:

    print("No")
