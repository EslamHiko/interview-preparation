
def solution(xs):
    # handle simple edge cases
    if len(xs) == 0:
        return str(0)
    if len(xs) == 1:
        return str(xs[0])

    # split input into positive/negative lists
    pos_nums = []
    neg_nums = []
    for n in xs:
        if n > 0: pos_nums.append(n)
        elif n < 0: neg_nums.append(n)

    # cache list counts
    pos_count = len(pos_nums)
    neg_count = len(neg_nums)

    # handle single negative panel edge case
    if neg_count == 1 and pos_count == 0:
        return str(0)

    # handle all zeros edge case
    if neg_count == 0 and pos_count == 0:
        return str(0)

    # calculate positive power output
    power_output = 1
    for n in pos_nums:
        power_output *= n

    # remove "largest" negative panel in odd arrangements
    if neg_count % 2 == 1:
        neg_nums.remove(max(neg_nums))

    # calculate negative power output
    for n in neg_nums:
        power_output *= n

    return str(power_output)
print(solution([2, 0, 2, 2, 0]))
