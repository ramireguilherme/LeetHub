def count_inversions(arr):
    if len(arr) < 2:
        return arr, 0
    
    mid = len(arr) // 2
    left, left_inv = count_inversions(arr[:mid])
    right, right_inv = count_inversions(arr[mid:])
    merged, split_inv = merge_and_count(left, right)
    
    return merged, left_inv + right_inv + split_inv

def merge_and_count(left, right):
    merged = []
    i = j = 0
    inversions = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            inversions += len(left) - i
            j += 1
    
    merged.extend(left[i:])
    merged.extend(right[j:])
    
    return merged, inversions

def find_fined_cars(n, entry, exit):
    entry_pos = {car: i for i, car in enumerate(entry)}
    
    exit_pos = [entry_pos[car] for car in exit]
    
    _, num_inversions = count_inversions(exit_pos)
    
    return num_inversions

n = int(input())
entry = list(map(int, input().split()))
exit = list(map(int, input().split()))

result = find_fined_cars(n, entry, exit)
print(result)
