def is_triangle(n_people, who_likes_who):
    for i in range(1, n_people + 1):
        a = who_likes_who[i - 1]  
        b = who_likes_who[a - 1] 
        c = who_likes_who[b - 1]  
        if c == i and a != b and b != c:
            return 'YES'
    return 'NO'

n_people = int(input())
people = list(map(int, input().split()))
print(is_triangle(n_people, people))
