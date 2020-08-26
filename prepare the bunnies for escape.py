
def shortest_path(sx, sy, map):
    h = len(map)
    w = len(map[0])
    b = [[None for i in range(w)] for i in range(h)]
    b[sx][sy] = 1

    a = [(sx, sy)]
    while a:
        x,y = a.pop(0)

        for i in [[1,0],[-1,0],[0,-1],[0,1]]:
            dx, dy = x+i[0], y+i[1]
            if 0 <= dx < h and 0 <= dy < w:

                if b[dx][dy] is None:
                    b[dx][dy] = b[x][y] + 1
                    if map[dx][dy] == 1: continue
                    a.append((dx, dy))

    return b

def solution(map):
    h = len(map)
    w = len(map[0])

    s = shortest_path(0, 0, map)
    f = shortest_path(h-1, w-1, map)
    board = []

    r = 2 ** 32-1
    for i in range(h):
        for j in range(w):
            if s[i][j] and f[i][j]: r = min(s[i][j]+f[i][j]-1, r)

    return r
