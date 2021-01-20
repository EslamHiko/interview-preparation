'''
For a given list of integers and integer K, find the number of non-empty subsets S such that min(S) + max(S) <= K.

Example 1:

nums = [2, 4, 5, 7]
k = 8
Output: 5
Explanation: [2], [4], [2, 4], [2, 4, 5], [2, 5]
Example 2:

nums = [1, 4, 3, 2]
k = 8
Output: 15
Explanation: 16 (2^4) - 1 (empty set) = 15
Example 3:

nums = [2, 4, 2, 5, 7]
k = 10
Output: 27
Explanation: 31 (2^5 - 1) - 4 ([7], [5, 7], [4, 5, 7], [4, 7]) = 27
Expected O(n^2) time solution or better.
'''

def genSubs(l):
    if not len(l):
        return [[]]
    x = genSubs(l[1:])
    return x+[[l[0]] + y for y in x]

def sol(arr,k):
    arr.sort()
    subsets = genSubs(arr)
    result = []
    for s in subsets:
        if len(s):
            if s[0] + s[-1] <= k:
                result.append(s)
    return result,len(result)

print(sol([2, 4, 5, 7],8))
print(sol([1, 4, 3, 2],8))
print(sol([2, 4, 2, 5, 7],10))
import math
def anotherSol(arr,k):
    lo = 0
    hi = len(arr)-1
    count = 0
    arr.sort()
    while lo <= hi:
        sum = arr[lo]+arr[hi]
        if sum <= k:
            count += math.pow(2,hi-lo)
            lo+=1
            continue
        if sum > k:
            hi -= 1

    return count
print(anotherSol([2, 4, 5, 7],8))
print(anotherSol([1, 4, 3, 2],8))
print(anotherSol([2, 4, 2, 5, 7],10))
