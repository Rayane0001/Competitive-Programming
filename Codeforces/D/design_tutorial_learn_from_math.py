def is_composite(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num%i == 0:
            return True
    return False

n = int(input())

x = n // 2
y = n - x

while not (is_composite(x) and is_composite(y)):
    x -= 1
    y += 1

print(f"{x} {y}")