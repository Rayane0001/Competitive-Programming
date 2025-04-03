from itertools import permutations

f, s = map(int,input().split())
steps = {int(input()) for _ in range(s)}
floors = list(range(1,f))
valid_routes = []

for perm in permutations(floors):
    route=[0] +list(perm)+ [0]
    if all(route[i+1] - route[i] in steps for i in range(len(route)-1)):
        valid_routes.append(route)

for route in sorted(valid_routes):
    print(" ".join(map(str, route)))
