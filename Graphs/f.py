
def horizontal_distance(x1, x2):
    return abs(x2 - x1)
def vertical_distance(y1, y2):
    return abs(y2 - y1)

xi, yi , xf, yf = map(int, input().split())
rook_moves = 2 if xi != xf and yi != yf else 1
bishop_moves = 0
if (xi + yi) % 2 == (xf + yf) % 2:
    if abs(xi - xf) == abs(yi - yf):
        bishop_moves = 1
    else:
        bishop_moves = 2
king_moves = max(horizontal_distance(xi,xf), vertical_distance(yi,yf))

print(rook_moves, bishop_moves, king_moves)