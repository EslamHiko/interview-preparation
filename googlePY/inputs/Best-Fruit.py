from collections import defaultdict
import math


def solve(N, M, A):
    favorites = [row[::-1] for row in A]
    remaining = set(range(1, N + 1))

    for r in range(N - 1):
        candidate_votes = {num: 0 for num in remaining}

        for row in favorites:
            while row[-1] not in remaining:
                row.pop()

            candidate_votes[row[-1]] += 1

        eliminate_num = -1
        eliminate_votes = math.inf

        for num, votes in candidate_votes.items():
            if votes < eliminate_votes or (
                votes == eliminate_votes and num < eliminate_num
            ):
                eliminate_num, eliminate_votes = num, votes

        remaining.discard(eliminate_num)

    return remaining.pop()


C = int(input())

for c in range(1, C + 1):
    input()
    N, M = map(int, input().split(" "))
    A = [list(map(int, input().split(" "))) for _ in range(M)]

    print(f"Case {c}: {solve(N, M, A)}")
