username = input().strip()
unique_chars = set(username)

if len(unique_chars) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")