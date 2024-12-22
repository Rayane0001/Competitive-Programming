def solve():
    n = int(input())
    movies = []

    for _ in range(n):
        a, b = map(int, input().split())
        movies.append((a, b))

    movies.sort(key=lambda x: x[1])

    count = 0
    last_end_time = 0

    for start, end in movies:
        if start >= last_end_time:
            count += 1
            last_end_time = end

    print(count)

solve()
