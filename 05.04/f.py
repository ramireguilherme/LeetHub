tests = int(input())
for __ in range(tests):
    collumns, x = map(int, input().split())
    heights = list(map(int, input().split()))
    left, right = 1, max(heights) + x
    while left < right:
        mid = (left + right + 1) // 2
        total_water = sum(max(0, mid - height) for height in heights)
        if total_water <= x:
            left = mid
        else:
            right = mid - 1  
    print(left) 
