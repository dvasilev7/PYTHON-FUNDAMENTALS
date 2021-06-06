numbers_input = input()
numbers_list_user = numbers_input.split()
numbers_list_final = []
for i in range(len(numbers_list_user)):
    current_number = int(numbers_list_user[i]) * -1
    numbers_list_final.append(current_number)
print(numbers_list_final)




