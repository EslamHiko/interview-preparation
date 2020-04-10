'''
ref : https://leetcode.com/discuss/interview-question/394347/
'''
def sol(flowers, cap1, cap2):
    can1 = cap1
    can2 = cap2
    refill = 2

    for i in range(len(flowers)/2):
        if can1 < flowers[i]:
            can1 = cap1
            refill += 1
        can1 -= flowers[i]

        if can2 < flowers[len(flowers)-i-1]:
            can2 = cap2
            refill += 1
        can2 -= flowers[len(flowers)-i-1]

    if len(flowers) % 2 == 1:
        if (can1 + can2) < flowers[len(flowers)/2]:
            refill += 1

    return refill

print(sol([2,4,5,1,2],5,7))
