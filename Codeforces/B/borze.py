borze = list(str(input()))
word = []
i = 0

while i < len(borze):
    if borze[i] == ".":
        word.append("0")
        i += 1
    elif borze[i] == "-":
        if i + 1 < len(borze) and borze[i + 1] == ".":
            word.append("1")
            i += 2
        else:
            word.append("2")
            i += 2

print("".join(word))
