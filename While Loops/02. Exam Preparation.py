count_of_error = int(input())
count_of_failed = 0
count_of_passed = 0
grade_sum = 0
grade_count = 0
name = 0
command = input()
while command != "Enough":
    grade = int(input())
    grade_sum += grade
    grade_count += 1
    if grade <= 4:
        count_of_failed += 1
    else:
        count_of_passed += 1
    if count_of_error - count_of_failed <= 0:
        print(f"You need a break, {int(count_of_failed)} poor grades.")
        break
    name = command
    command = input()
else:
    print(f"Average score: {grade_sum / grade_count:.2f}")
    print(f"Number of problems: {int(count_of_passed + count_of_failed)}")
    print(f"Last problem: {name}")

