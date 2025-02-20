import sys
input = sys.stdin.read

def count_common_cds(data):
    lines = data.split()
    index = 0
    results = []
    
    while True:
        N = int(lines[index])
        M = int(lines[index + 1])
        index += 2
        
        if N == 0 and M == 0:
            break
        
        jacks_cds = []
        for _ in range(N):
            jacks_cds.append(int(lines[index]))
            index += 1
        
        jills_cds = []
        for _ in range(M):
            jills_cds.append(int(lines[index]))
            index += 1
        
        i, j = 0, 0
        common_count = 0
        while i < N and j < M:
            if jacks_cds[i] < jills_cds[j]:
                i += 1
            elif jacks_cds[i] > jills_cds[j]:
                j += 1
            else:
                common_count += 1
                i += 1
                j += 1
        
        results.append(common_count)
    
    return results

if __name__ == "__main__":
    import sys
    data = sys.stdin.read()
    results = count_common_cds(data)
    for result in results:
        print(result)
