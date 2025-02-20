def digit_sum(x):
    return sum(int(d) for d in str(x))

tests = int(input())
test_cases = [int(input()) for _ in range(tests)]
max_n = max(test_cases)
digit_sums = [0] * (max_n + 1)
prefix_sum = [0] * (max_n + 1)
for i in range(1, max_n + 1):
    digit_sums[i] = digit_sum(i)
    prefix_sum[i] = prefix_sum[i - 1] + digit_sums[i]

results = [str(prefix_sum[n]) for n in test_cases]
print("\n".join(results))

