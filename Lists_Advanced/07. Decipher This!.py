text = input().split()
for word in text:
    first_letter_list = []
    [first_letter_list.append(character) for character in word if character.isnumeric()]
    first_letter = list(chr(int("".join(first_letter_list))))
    rest_of_word = list(filter(lambda character: character.isalpha(), word))
    full_word = first_letter + rest_of_word
    full_word[1], full_word[-1] = full_word[-1], full_word[1]
    print("".join(full_word), end=" ")