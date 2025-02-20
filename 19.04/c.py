size, sliding = map(int, input().split())
arr = list(map(int, input().split()))
sliding_sum = sum(arr[:sliding])
min_sum = sliding_sum
min_sum_index = 0
for i in range(1, size - sliding + 1):
    sliding_sum = sliding_sum - arr[i - 1] + arr[i + sliding - 1]
    if sliding_sum < min_sum:
        min_sum = sliding_sum
        min_sum_index = i

print(min_sum_index + 1)
