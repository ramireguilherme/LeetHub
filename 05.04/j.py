queries = int(input())
for _ in range(queries):
    arr = list(map(int, input().split()))
    total_damage = sum(arr)
    round_number = 1
    while total_damage > 0 :
        damage = 1
        if round_number % 7 == 0:
            damage = 3
            arr[0] -= 1
            arr[1] -= 1
            arr[2] -= 1
        else:
            arr[arr.index(max(arr))] -= 1
        if arr[0] < 0 or arr[1] < 0 or arr[2] < 0:
            break
        total_damage -= damage
        round_number += 1

    print("YES" if (round_number-1) % 7 == 0 else "NO")