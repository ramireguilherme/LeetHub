def is_jolly(size, seq):
    if size == 1:
        return True
    differences = {}
    found_differences = 0
    
    for indice in range(len(seq)-1):
        difference = abs(seq[indice] - seq[indice+1])
        if difference not in differences and difference < size:
            found_differences += 1
            differences[difference] = True
        if found_differences == size -1:
            return True
    return False

while True:
    try:
        sequence = list(map(int,input().split()))
        n  = sequence[0]
        sequence = sequence[1:]
        print("Jolly" if is_jolly(n,sequence) else "Not jolly")
    except EOFError:
        break