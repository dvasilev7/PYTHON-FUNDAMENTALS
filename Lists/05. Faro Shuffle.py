cards = input()
shuffles = int(input())
cards_list = cards.split()
half = int(len(cards_list) / 2)
for i in range(shuffles):
    left_half = cards_list[:half]
    right_half = cards_list[half:]
    cards_list = []
    for index in range(len(left_half)):
        cards_list.append(left_half[index])
        cards_list.append(right_half[index])
print(cards_list)