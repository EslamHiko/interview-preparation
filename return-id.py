def solution(x,y):
    diff = y - 1
    cornerPos = x + diff
    id = cornerPos * (cornerPos + 1) // 2
    id -= diff
    return str(id)

solution(1,1)
solution(2,3)
