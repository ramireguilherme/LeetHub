def solve_case(A, B, C):
    # We need to iterate over possible values for x, y, and z.
    # To ensure x, y, and z are distinct, we limit our search.
    # A reasonable range for x, y, z would be [1, 100] because:
    # If x, y, z > 100, their sum would exceed 300, but A ≤ 10000.
    
    best_solution = None
    
    for x in range(-100, 101):
        for y in range(-100, 101):
            if x != y:
                for z in range(-100, 101):
                    if x != z and y != z:
                        if x + y + z == A and x * y * z == B and x**2 + y**2 + z**2 == C:
                            if best_solution is None or (x < best_solution[0] or 
                                                         (x == best_solution[0] and y < best_solution[1])):
                                best_solution = (x, y, z)
                                
    return best_solution

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    N = int(data[0])
    index = 1
    results = []
    
    for _ in range(N):
        A = int(data[index])
        B = int(data[index + 1])
        C = int(data[index + 2])
        index += 3
        
        solution = solve_case(A, B, C)
        if solution:
            results.append(f"{solution[0]} {solution[1]} {solution[2]}")
        else:
            results.append("No solution.")
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
