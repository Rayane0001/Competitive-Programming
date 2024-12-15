MOD = 10**9 + 7

n = int(input())

dp = [0] * (n + 1)
dp[0] = 1

for i in range(1, n + 1):
    dp[i] = (dp[i - 1] if i - 1 >= 0 else 0) + \
            (dp[i - 2] if i - 2 >= 0 else 0) + \
            (dp[i - 3] if i - 3 >= 0 else 0) + \
            (dp[i - 4] if i - 4 >= 0 else 0) + \
            (dp[i - 5] if i - 5 >= 0 else 0) + \
            (dp[i - 6] if i - 6 >= 0 else 0)
    dp[i] %= MOD

print(dp[n])