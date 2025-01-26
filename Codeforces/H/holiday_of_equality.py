n = int(input())
taxes = list(map(int, input().split()))
max_tax = max(taxes)
print(sum(max_tax - tax for tax in taxes if tax < max_tax))
