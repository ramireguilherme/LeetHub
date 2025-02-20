from collections import defaultdict, deque

def main():
    import sys
    input = sys.stdin.read
    data = input().split('\n')
    
    n = int(data[0].strip())
    
    graph = defaultdict(list)
    reverse_graph = defaultdict(list)
    indegree = defaultdict(int)
    
    # Parse each rule and build the graph
    for i in range(1, n+1):
        line = data[i].strip()
        if not line:
            continue
        parts = line.split(':')
        f = parts[0].strip()
        dependencies = parts[1].strip().split() if len(parts) > 1 else []
        
        for dep in dependencies:
            graph[f].append(dep)
            reverse_graph[dep].append(f)
            indegree[f] += 1

    # Changed file
    changed_file = data[n+1].strip()
    
    # Determine which files need to be recompiled using BFS on the reverse graph
    to_recompile = set()
    queue = deque([changed_file])
    
    while queue:
        file = queue.popleft()
        if file not in to_recompile:
            to_recompile.add(file)
            for dependent in reverse_graph[file]:
                if dependent not in to_recompile:
                    queue.append(dependent)
    
    # Topological sort of the recompiled files
    sorted_files = []
    zero_indegree_queue = deque([f for f in to_recompile if indegree[f] == 0])
    
    while zero_indegree_queue:
        node = zero_indegree_queue.popleft()
        sorted_files.append(node)
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0 and neighbor in to_recompile:
                zero_indegree_queue.append(neighbor)
    
    # Output the sorted files needing recompilation
    for file in sorted_files:
        print(file)

if __name__ == "__main__":
    main()
