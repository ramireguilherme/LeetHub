def solve(n, arr):
    iterations = 1
    start = arr[n-1]
    while start != n:
        start = arr[start-1]
        iterations += 1
    return iterations



queries = int(input())
for _ in range(queries):
    n = int(input())
    arr = list(map(int, input().split()))
    sol = [solve(i, arr) for i in range(1, n+1)]
    print(*sol)    
