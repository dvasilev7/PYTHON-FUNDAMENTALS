n = int(input())
grades = {}

for numbers in range(n):
    name = input()
    score = input()
    grade = float(score)
    if name not in grades:
        grades[name] = []
        grades[name].append(grade)
    else:
        grades[name].append(grade)

filtered_students = {key: value for (key, value) in grades.items() if sum(value) / len(value) >= 4.50}
sorted_grades = dict(sorted(filtered_students.items(), key=lambda x: sum(x[1]) / len(x[1]), reverse=True))

for key, value in sorted_grades.items():
    print(f"{key} -> {sum(value) / len(value):.2f}")