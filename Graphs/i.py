from collections import defaultdict, deque

def find_custom_lexicographical_order(names):
    n = len(names)
    graph = defaultdict(set)
    indegree = defaultdict(int)

    for name in names:
        for char in name:
            if char not in indegree:
                indegree[char] = 0

    for i in range(n - 1):
        name1, name2 = names[i], names[i + 1]
        min_length = min(len(name1), len(name2))
        for j in range(min_length):
            if name1[j] != name2[j]:
                if name2[j] not in graph[name1[j]]:
                    graph[name1[j]].add(name2[j])
                    indegree[name2[j]] += 1
                break
        else:  
            if len(name1) > len(name2):
                return "Impossible"  

    zero_indegree = deque([char for char in indegree if indegree[char] == 0])
    order = []

    while zero_indegree:
        current = zero_indegree.popleft()
        order.append(current)
        for neighbor in graph[current]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                zero_indegree.append(neighbor)

    if len(order) != len(indegree): 
        return "Impossible"

    all_letters = set('abcdefghijklmnopqrstuvwxyz')
    order.extend(sorted(all_letters - set(indegree.keys())))
    
    return ''.join(order)

n = int(input().strip())
names = [input().strip() for _ in range(n)]
print(find_custom_lexicographical_order(names))
