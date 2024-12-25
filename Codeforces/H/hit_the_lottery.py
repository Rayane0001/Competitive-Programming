# THE SMART WAY :
n = int(input())
denominations = [100, 20, 10, 5, 1]
bills = 0

for denom in denominations:
    bills += n // denom
    n %= denom

print(bills)

# THE DUMB WAY :
# n = int(input())
# denominations = [1, 5, 10, 20, 100]
# bills = 0
# while n >= 1:
#     if n >= 100:
#         n -= 100
#         bills += 1
#     elif 20 <= n < 100:
#         n -= 20
#         bills += 1
#     elif 10 <= n < 20:
#         n -= 10
#         bills += 1
#     elif 5 <= n < 10:
#         n -= 5
#         bills += 1
#     elif 1 <= n < 5:
#         n -= 1
#         bills += 1
# print(bills)