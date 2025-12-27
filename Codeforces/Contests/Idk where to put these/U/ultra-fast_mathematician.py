# tags: implementation

num1 = input().strip()
num2 = input().strip()

result = ""

for i in range(len(num1)):
    if num1[i] != num2[i]:
        result += "1"
    else:
        result += "0"

print(result)