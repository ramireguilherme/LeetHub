def solve(n, arr):
    start = 1
    start = arr[n-1]
    while start != n:
        start = arr[start-1]
        iterations += 1
        if iterations == 3:
            return True
    return False



n = int(input())
arr = list(map(int, input().split()))
sol = [solve(i, arr) for i in range(1, n+1)]
print(*sol)    
