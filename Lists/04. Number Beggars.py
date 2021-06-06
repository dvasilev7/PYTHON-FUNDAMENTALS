numbers = input()
beggars_count = int(input())
beggars_list = list(range(beggars_count))
numbers_list = numbers.split(", ")
final_list = []
for beggar in range(beggars_count):
    list_per_beggar = []
    for num in range(beggar, len(numbers_list), beggars_count):
        list_per_beggar.append(int(numbers_list[num]))
    sum_per_beggar = sum(list_per_beggar)
    final_list.append(sum_per_beggar)
print(final_list)
