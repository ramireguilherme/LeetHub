n_logs = int(input())
logs = []
winner = ""
potential_winners = []
highest_score = 0
players = 0
for _ in range(n_logs):
    logs.append(input().split())
scores = {}
for log in logs:
    name, score = log
    score = int(score)
    if name not in scores:
        scores[name] = score
        players += 1
    else:
        scores[name] += score
    if scores[name] < 0:
        players -= 1
    if scores[name] > highest_score:
        highest_score = scores[name]
        winner = name
        potential_winners = []
    if scores[name] == highest_score:
        potential_winners.append(name)