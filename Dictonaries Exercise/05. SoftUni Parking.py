registered_users = {}
number_of_commands = int(input())
for i in range(number_of_commands):
    command = input()
    action_list = command.split()
    if action_list[0] == "register":
        username = action_list[1]
        licensePlateNumber = action_list[2]
        if username not in registered_users:
            registered_users[username] = licensePlateNumber
            print(f"{username} registered {licensePlateNumber} successfully")
        else:
            print(f"ERROR: already registered with plate number {licensePlateNumber}")
    if action_list[0] == "unregister":
        username = action_list[1]
        if username not in registered_users:
            print(f"ERROR: user {username} not found")
        else:
            registered_users.pop(username)
            print(f"{username} unregistered successfully")

for key, value in registered_users.items():
    print(f"{key} => {value}")


