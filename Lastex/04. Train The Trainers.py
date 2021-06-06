jury_persons = int(input())
all_presentation_sum = 0
all_score_average = 0
project_count = 0
presentation_name = input()
while presentation_name != "Finish":
    sum_score = 0
    average_score = 0
    project_count += 1
    for persons in range(1, jury_persons + 1):
        score = float(input())
        sum_score += score
        average_score = sum_score / jury_persons
        all_presentation_sum += score
    all_score_average = all_presentation_sum / (jury_persons * project_count)
    print(f"{presentation_name} - {average_score:.2f}.")
    presentation_name = input()
else:
    print(f"Student's final assessment is {all_score_average:.2f}.")
