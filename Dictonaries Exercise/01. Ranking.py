contests = {}
contest = input()
while contest != "end of contests":
    contest, password = contest.split(":")
    contests[contest] = password
    contest = input()

users = {}
submission = input()
while submission != "end of submissions":
    contests_new = {}
    contest, password, username, points = submission.split("=>")
    points = int(points)
    if contest in contests and password == contests[contest]:
        if username in users:
            ddict = users[username]
            if contest in ddict:
                if points > ddict[contest]:
                    contests_new[contest] = points
                    users[username].update(contests_new)
            else:
                contests_new[contest] = points
                users[username].update(contests_new)
        else:
            contests_new[contest] = points
            users[username] = contests_new
    submission = input()

total = 0
name = 0
for username in users:
    user_total = sum(users[username].values())
    users[username] = dict(sorted(users[username].items(), key=lambda item: item[1], reverse=True))
    if user_total > total:
        total = user_total
        name = username

users = dict(sorted(users.items()))

print(f"Best candidate is {name} with total {total} points.")
print("Ranking:")
for username in users:
    print(username)
    for contest in users[username]:
        final_contests = users[username]
        print(f"#  {contest} -> {final_contests[contest]}")