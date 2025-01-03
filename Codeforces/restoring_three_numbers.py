x = list(map(int, input().split()))

x.sort()

total_sum = x[3]

a = total_sum - x[1]
b = total_sum - x[2]
c = total_sum - x[0]

print(a, b, c)
