n_points = int(input())
points = []
for _ in range(n_points):
    x, y = map(int, input().split())
    points.append((x, y))
point_set = set(points)
count = 0
for i in range(n_points):
    for j in range(i + 1, n_points):
        x1, y1 = points[i]
        x2, y2 = points[j]
        if (x1 + x2) % 2 == 0 and (y1 + y2) % 2 == 0:
            x3 = (x1 + x2) // 2
            y3 = (y1 + y2) // 2
            
            if (x3, y3) in point_set:
                count += 1

print(count)