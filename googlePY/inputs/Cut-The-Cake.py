from functools import lru_cache


def solve(H, W, K, A):
    strawberry_count = [[0] * (W + 1) for _ in range(H + 1)]

    for y, row in enumerate(A, 1):
        for x, val in enumerate(row, 1):
            strawberry_count[y][x] = (
                val
                + strawberry_count[y - 1][x]
                + strawberry_count[y][x - 1]
                - strawberry_count[y - 1][x - 1]
            )

    def contains_strawberry(y0, y1, x0, x1):
        return bool(
            strawberry_count[y1][x1]
            - strawberry_count[y0][x1]
            - strawberry_count[y1][x0]
            + strawberry_count[y0][x0]
        )

    @lru_cache(None)
    def count_cuts(y, x, k):
        if k == 1:
            return int(contains_strawberry(y, H, x, W))
        if y == H or x == W:
            return 0

        return sum(
            count_cuts(y_mid, x, k - 1)
            for y_mid in range(y + 1, H + 1)
            if contains_strawberry(y, y_mid, x, W)
        ) + sum(
            count_cuts(y, x_mid, k - 1)
            for x_mid in range(x + 1, W + 1)
            if contains_strawberry(y, H, x, x_mid)
        )

    return count_cuts(0, 0, K)


C = int(input())

for c in range(1, C + 1):
    input()
    H, W, K = map(int, input().split(" "))
    A = [[x == "v" for x in input()] for _ in range(H)]

    print(f"Case {c}: {solve(H, W, K, A)}")
