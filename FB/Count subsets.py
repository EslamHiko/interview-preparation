'''
/*question:


Input:

Given an array A of
-positive
-sorted
-no duplicate
-integer

A positive integer k


Output:

Count of all such subsets of A,
Such that for any such subset S,
Min(S) + Max(S) = k
subset should contain atleast two elements

1. Backtracking approach to get subsets
2. Get min and max of subset
3. Add min and max and put them in Hashmap (or update the count)
4. repeat this process for all subsets
5. search for k in hashmap and return count of k

input: {1,2,3,4,5}

subsets:
1, 2, 3, 4, 5, {1,2},{1,3}
k = 5

count = 5

{1, 4},{2,3} {1,2,4}, {1,2,3,4} {1,3,4}

*/
'''
def subs(l):
    if l == []:
        return [[]]

    x = subs(l[1:])

    return x + [[l[0]] + y for y in x]

def sol(arr,k):
    results = []
    arr.sort()
    subsets = subs(arr)

    for s in subsets:
        if len(s) >= 2:
            if s[0] + s[-1] == k:
                results.append(s)

    return results,len(results)

print(sol([1,2,3,4,5],5))

import math

def anotherSol(arr,k):
    hi = len(arr)-1
    lo = 0
    count = 0

    while lo < hi and hi-lo > 0:
        sum = arr[hi] + arr[lo]
        if sum == k:
            count += math.pow(2,(hi-lo)-1)
            lo += 1
            hi -= 1
            continue

        if sum > k:
            hi -= 1
        else:
            lo += 1

    return count

print(anotherSol([1,2,3,4,5],5))
