# Read input values
k, n, w = map(int, input().strip().split())

# Calculate the total cost of w bananas
total_cost = k * w * (w + 1) // 2

borrow = total_cost - n

if borrow < 0:
    borrow = 0

print(borrow)