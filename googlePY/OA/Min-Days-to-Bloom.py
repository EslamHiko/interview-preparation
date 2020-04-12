'''
Given an array of roses. roses[i] means rose i will bloom on day roses[i]. Also given an int k, which is the minimum number of adjacent bloom roses required for a bouquet, and an int n, which is the number of bouquets we need. Return the earliest day that we can get n bouquets of roses.

Example:
Input: roses = [1, 2, 4, 9, 3, 4, 1], k = 2, n = 2
Output: 4
Explanation:
day 1: [b, n, n, n, n, n, b]
The first and the last rose bloom.

day 2: [b, b, n, n, n, n, b]
The second rose blooms. Here the first two bloom roses make a bouquet.

day 3: [b, b, n, n, b, n, b]

day 4: [b, b, b, n, b, b, b]
Here the last three bloom roses make a bouquet, meeting the required n = 2 bouquets of bloom roses. So return day 4.

int minDaysBloom(int[] roses, int k, int n) {
}
'''
def sol(roses,k,n):
    maxBouquets = 0
    currDay = 0
    while maxBouquets < n:
        currDay += 1
        adjacent = False
        adjacentCount = 0
        maxBouquets = 0
        for i in range(len(roses)):
            if(roses[i] == currDay):
                roses[i] = 'b'

            if (roses[i] == 'b' and not adjacent) or (adjacent and roses[i] == 'b'):
                adjacent = True
                adjacentCount += 1
                if adjacentCount == k:
                    maxBouquets += 1
                    adjacentCount = 0

            if roses[i] != 'b':
                adjacent = False
                adjacentCount = 0

    return currDay,roses

print(sol([1, 2, 4, 9, 3, 4, 1],2,2))
print(sol([1, 2, 1, 1, 3, 4, 1],2,2))
print(sol([1, 2, 2, 1, 3, 1, 1],2,2))
