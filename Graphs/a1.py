def find_student_with_two_holes(n, p):
    results = []
    
    for start in range(1, n+1):
        visited = set()
        current = start
        
        while current not in visited:
            visited.add(current)
            current = p[current - 1]  

        results.append(current) 

    return results

n = int(input())
data = input().split()
p = list(map(int, data))

result = find_student_with_two_holes(n, p)
print(' '.join(map(str, result)))

