def count_divisible_subarrays(n, arr):
    prefix = [0] * n
    modulo_counts = [0] * n
    prefix[0] = arr[0] % n
    modulo_counts[prefix[0] % n] += 1

    for i in range(1, n):
        prefix[i] = (prefix[i-1] + arr[i]) % n
        modulo_counts[prefix[i] % n] += 1

    result = 0
    for m in range(n):
        if modulo_counts[m] > 1:
            result += modulo_counts[m] * (modulo_counts[m] - 1) // 2
        if m == 0:
            result += modulo_counts[m]

    return result

n = int(input())
arr = list(map(int, input().split()))
print(count_divisible_subarrays(n, arr))