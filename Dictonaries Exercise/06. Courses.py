command = input()
courses = {}
while command != "end":
    course, name = command.split(" : ")
    if course not in courses:
        courses[course] = []
        courses[course].append(name)
    else:
        courses[course].append(name)
    command = input()
    courses[course].sort()

courses = dict(sorted(courses.items(), key=lambda item: len(item[1]), reverse=True))

for key, value in courses.items():
    print(f"{key}: {len(value)}")
    [print(f"-- {el}") for el in value]
