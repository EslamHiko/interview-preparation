'''
Problem Statement #
Given a set with distinct elements, find all of its distinct subsets.

Example 1:

Input: [1, 3]
Output: [], [1], [3], [1,3]
Example 2:

Input: [1, 5, 3]
Output: [], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3]
'''
# subsets
def solve(arr):
    result = [[]]
    for i in range(len(arr)):
        for j in range(i+1,len(arr)+1):
            result.append(arr[i:j])

    return result

print(solve([1, 3]))
print(solve([1, 5, 3]))

def solve2(arr):
    subsets = []
    subsets.append([])
    for el in arr:
        n = len(subsets)
        for j in range(n):
            currSet = list(subsets[j])
            currSet.append(el)

            subsets.append(currSet)
    return subsets

print(solve2([1, 3]))
print(solve2([1, 5, 3]))
