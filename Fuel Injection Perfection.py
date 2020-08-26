def solution(n):
    n = long(n)
    count = 0
    while n > 3:
        if n & 1:
            if n & 2:
                n = (n + 1) >> 2
                count += 3
            else:
                n = (n - 1) >> 1
                count += 2
        else:
            n = n >> 1
            count += 1

    if n == 3:
        n = n - 1
        count += 1

    if n == 2:
        n = n - 1
        count += 1

    return count

print(solution(15))
print(solution(4))
