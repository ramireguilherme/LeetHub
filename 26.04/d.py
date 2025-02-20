from collections import defaultdict
n, k = map(int, input().split())
arr = list(map(int, input().split()))
left = 0
right = 0
freq_map = defaultdict(int)
num_distinct = 0
count_subarrays = 0
while right < n:
    if freq_map[arr[right]] == 0:
        num_distinct += 1
    freq_map[arr[right]] += 1
    
    while num_distinct > k:
        freq_map[arr[left]] -= 1
        if freq_map[arr[left]] == 0:
            num_distinct -= 1
        left += 1
    
    count_subarrays += (right - left + 1)
    right += 1
    
print(count_subarrays)
