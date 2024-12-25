# number of levels
n = int(input())

# levels X can pass
p = list(map(int, input().split()))[1:]

# levels Y can pass
q = list(map(int, input().split()))[1:]

# Combine levels X and Y can pass
passing_levels = set(p).union(set(q))

# Check if they can pass all levels
if set(range(1, n + 1)) == passing_levels:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")