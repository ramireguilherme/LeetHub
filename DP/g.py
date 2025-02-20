
tests =  int(input())
for _ in range(tests):
    n_weights = int(input())
    weights = []
    values = []
    result = 0
    for _ in range(n_weights):
        value , weight = map(int, input().split())
        weights.append(weight)
        values.append(value)
    n = len(values)
    people = int(input())
    max_weights = []
    for __ in range(people):
        max_weights.append(int(input()))
    dp = [[0 for _ in range(max(max_weights) + 1)] for _ in range(n + 1)]

    for weight in max_weights:
        max_weight = weight
        for i in range(1, n + 1):
            for w in range(max_weight + 1):
                if weights[i-1] <= w:
                    dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + values[i-1])
                else:
                    dp[i][w] = dp[i-1][w]

        person_max = dp[n][max_weight]
        result += person_max
    print(result)