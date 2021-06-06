change = float(input())
count_of_coins = 0
change = int(change * 100)
while change > 1:
    count_of_coins += change // 200
    change = change % 200
    count_of_coins += change // 100
    change = change % 100
    count_of_coins += change // 50
    change = change % 50
    count_of_coins += change // 20
    change = change % 20
    count_of_coins += change // 10
    change = change % 10
    count_of_coins += change // 5
    change = change % 5
    count_of_coins += change // 2
    change = change % 2
if change == 1:
    count_of_coins += 1
print(int(count_of_coins))
