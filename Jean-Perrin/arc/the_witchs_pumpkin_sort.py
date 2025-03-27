a = int(input())
weights = list(map(int, input().split()))

i_weights = [(weights[i], i + 1) for i in range(a)]

i_weights.sort()

sorted_i=[index for weight, index in i_weights]

print(*sorted_i)