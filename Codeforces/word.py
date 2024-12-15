word = input().strip()

lowercases = sum(1 for c in word if c.islower())
uppercases = sum(1 for c in word if c.isupper())

if lowercases >= uppercases:
    word = word.lower()
elif uppercases > lowercases:
    word = word.upper()

print(word)