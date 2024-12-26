n = int(input())
teams = []

for _ in range(n):
    h, a = map(int, input().split())
    teams.append((h, a))

count = 0
for host in range(n):
    for guest in range(n):
        if host != guest:
            host_home = teams[host][0]
            guest_away = teams[guest][1]

            if host_home == guest_away:
                count += 1

print(count)