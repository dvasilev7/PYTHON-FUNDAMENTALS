import re

text = input()

pattern1 = r"([:]{2}|[*]{2})([A-Z]{1}[a-z]{2,})(\1)"
pattern2 = r"\d"
emoji_dict = re.findall(pattern1, text)
cool_emojis = []

cool_threshold = 1

cool_threshold_list = re.findall(pattern2, text)
for number in cool_threshold_list:
    cool_threshold *= int(number)

for emoji in emoji_dict:
    emoji_sum = 0
    for symbol in emoji[1]:
        emoji_sum += ord(symbol)
    if emoji_sum > cool_threshold:
        cool_emojis.append(emoji)


print(f"Cool threshold: {cool_threshold}")
print(f"{len(emoji_dict)} emojis found in the text. The cool ones are:")
if len(cool_emojis) > 0:
    for emoji in cool_emojis:
        print(''.join(emoji))