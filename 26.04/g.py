



n = int(input())
coin_values = list(map(int,input().split()))

max_sum = sum(coin_values)
possible = [False] * (max_sum + 1)
possible[0] = True

for coin in coin_values:
    for j in range(max_sum, coin - 1, -1):
        if possible[j - coin]:
            possible[j] = True

result_sums = [i for i in range(max_sum + 1) if possible[i]]

print(len(result_sums)-1)
print(" ".join(map(str, result_sums[1:])))

