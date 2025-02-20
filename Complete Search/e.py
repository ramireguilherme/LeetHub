import heapq

def kth_smallest_pair(arr, k, n):
    if k == 1:
        return arr[0]
    if k == n:
        return arr[-1]
    
    heap = []
    for i in range(n):
        for j in range(i+1, n):
            if len(heap) < k:
                heapq.heappush(heap, -1*(arr[i] * arr[j]))
            else:
                if -1*(arr[i] * arr[j]) > heap[0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, -1*(arr[i] * arr[j]))
    
    return -1*heap[0]

tests =  int(input())
for __ in range(tests):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    print(kth_smallest_pair(arr, k, n))