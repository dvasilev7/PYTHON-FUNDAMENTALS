total_steps = 0
command = input()
while command != "Going home":
    steps = int(command)
    total_steps += steps
    if total_steps >= 10000:
        break
    command = input()
else:
    final_steps = int(input())
    total_steps += final_steps

if total_steps < 10000:
    print(f"{10000 - total_steps} more steps to reach goal.")
else:
    print("Goal reached! Good job!")
    print(f"{total_steps - 10000} steps over the goal!")