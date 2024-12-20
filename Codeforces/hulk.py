# tags: implementation

n = int(input())
result = ""

for i in range(n):
    if i % 2 == 0:
        result += "I hate"
    else:
        result += "I love"
    if i != n - 1:
        result += " that "

result += " it"
print(result)