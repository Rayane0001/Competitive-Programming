t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    layers = [1]
    while layers[-1] < sum(a):
        layers.append(layers[-1] + 8 * len(layers))

    happy_days = 0
    assembled_pieces = 0

    for pieces in a:
        assembled_pieces += pieces
        if assembled_pieces in layers:
            happy_days += 1

    print(happy_days)
