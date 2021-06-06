tabs = int(input())
salary = int(input())
for numbers in range(1, tabs + 1):
    site_name = input()
    if site_name == "Facebook":
        salary -= 150
    if site_name == "Instagram":
        salary -= 100
    if site_name == "Reddit":
        salary -= 50
if salary > 0:
    print(f"{int(salary)}")
else:
    print("You have lost your salary.")