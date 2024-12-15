n = int(input().strip())
s = input().strip()

removals = 0

for i in range(1, n):
    if s[i] == s[i - 1]:
        removals += 1

print(removals)