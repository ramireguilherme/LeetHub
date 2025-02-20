def form_teams(n, skills):
    programmers = []
    mathematicians = []
    sportsmen = []

    for i in range(n):
        if skills[i] == 1:
            programmers.append(i + 1)
        elif skills[i] == 2:
            mathematicians.append(i + 1)
        elif skills[i] == 3:
            sportsmen.append(i + 1)

    num_teams = min(len(programmers), len(mathematicians), len(sportsmen))

    teams = []
    for i in range(num_teams):
        team = (programmers[i], mathematicians[i], sportsmen[i])
        teams.append(team)

    print(num_teams)
    for team in teams:
        print(team[0], team[1], team[2])

n = int(input())
skills = list(map(int, input().split()))
form_teams(n, skills)
