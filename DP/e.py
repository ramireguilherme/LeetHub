import math

t = int(input())

MAX_N = 10000

dp = [float('inf')] * (MAX_N + 1)
dp[0] = 0

for i in range(1, MAX_N + 1):
    j = 1
    while j * j <= i:
        dp[i] = min(dp[i], dp[i - j * j] + 1)
        j += 1

for line in range(t):
    N = int(input())
    print(dp[N])
