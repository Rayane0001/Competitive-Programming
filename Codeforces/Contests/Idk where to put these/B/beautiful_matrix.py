# tags: implementation

# TODO : à refaire potentiellement
matrix = []
for i in range(5):
    row = list(map(int, input().split()))
    matrix.append(row)

for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            x, y = i, j
            break

moves = abs(x-2) + abs(y-2)

print(moves)