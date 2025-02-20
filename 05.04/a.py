
n = int(input())
numbers = list(map(int, input().split()))

even_count = 0
odd_count = 0
even_index = -1
odd_index = -1

for i in range(n):
    if numbers[i] % 2 == 0:
        even_count += 1
        if even_count == 1:
            even_index = i + 1
    else:
        odd_count += 1
        if odd_count == 1:
            odd_index = i + 1

if even_count == 1:
    print(even_index)
else:
    print(odd_index)

