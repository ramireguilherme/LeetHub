n_logs =  int(input())
scores = {}
score_history = {}
max_score = 0
winner = ""
n_players = 0
for _ in range(n_logs):
    name, score = input().split()
    score = int(score)
    if name not in scores:
        scores[name] = score
        n_players += 1
        score_history[name] = []
        score_history[name].append(score)
    else:
        scores[name] += score
        score_history[name].append(scores[name])

    if scores[name] < 0:
        n_players -= 1
    if scores[name] > max_score:
        max_score = scores[name]
        winner = name
    
    candidates = [name for name, score in scores.items() if score == max_score]
    
    earliest_round = float('inf')
    winner = None
    
    for candidate in candidates:
        for score in score_history[candidate]:
            if score >= max_score:
                if round < earliest_round:
                    earliest_round = round_number
                    winner = candidate
                break
print(winner)