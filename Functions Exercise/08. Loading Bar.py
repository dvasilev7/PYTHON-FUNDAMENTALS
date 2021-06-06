def fill_bar(bar, bars):
    for index in range(bars_to_fill):
        bar_list[index] = "%"
    return bar_list


bar_list = []
for num in range(10):
    bar_list.append(".")

percent = int(input())
bars_to_fill = percent // 10
filled = fill_bar(bar_list, bars_to_fill)
if percent < 100:
    print(f"{percent}% [{''.join(filled)}]")
    print("Still loading...")
else:
    print("100% Complete!")
    print(f"[{''.join(filled)}]")