def count_ways(x, coins):
    MOD = 10**9 + 7
    dp = [0] * (x + 1)
    dp[0] = 1
    for coin in coins:
        for j in range(coin, x + 1):
            dp[j] = (dp[j] + dp[j - coin]) % MOD
    return dp[x]

n, x = map(int, input().split())
coins = map(int, input().split())
print(count_ways(x, coins))
