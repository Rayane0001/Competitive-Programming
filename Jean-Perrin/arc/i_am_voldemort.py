import math

t = int(input().strip())
for _ in range(t):
    encoded = input().strip()
    n = int(math.sqrt(len(encoded)))
    matrix = [encoded[i * n:(i + 1) * n] for i in range(n)]
    decoded = []
    for i in range(n):
        for j in range(n):
            decoded.append(matrix[j][n - 1 - i])
    print("".join(decoded))
