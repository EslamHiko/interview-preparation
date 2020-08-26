import collections
def solution(data,n):
    map = collections.defaultdict(lambda: 0)
    for el in data:
        map[el] += 1
    return [el for el in data if map[el] <= n]
