cards = input()
list_of_cards = cards.split()
list_of_players_A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
list_of_players_B = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
B_players = []
A_players = []
for i in range(len(list_of_cards)):
    new_list = list_of_cards[i].split("-")
    new_list[1] = int(new_list[1])
    if new_list[0] == "A":
        if new_list[1] not in A_players:
            list_of_players_A.pop()
        A_players.append(new_list[1])
    elif new_list[0] == "B":
        if new_list[1] not in B_players:
            list_of_players_B.pop()
        B_players.append(new_list[1])
    if len(list_of_players_A) < 7 or len(list_of_players_B) < 7:
        break

if len(list_of_players_A) >= 7 and len(list_of_players_B) >= 7:
    print(f"Team A - {len(list_of_players_A)}; Team B - {len(list_of_players_B)}")
else:
    print(f"Team A - {len(list_of_players_A)}; Team B - {len(list_of_players_B)}")
    print("Game was terminated")
