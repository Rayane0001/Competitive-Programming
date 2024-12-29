# tags: string
letters = input().strip("{}").replace(", ", "")
print(len(set(letters)))
