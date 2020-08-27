'''
Problem Statement #
Given a set of numbers that might contain duplicates, find all of its distinct subsets.

Example 1:

Input: [1, 3, 3]
Output: [], [1], [3], [1,3], [3,3], [1,3,3]
Example 2:

Input: [1, 5, 3, 3]
Output: [], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3], [3,3], [1,3,3], [3,3,5], [1,5,3,3]
'''

def solve(arr):
    result = [[]]
    exists = {'':1}

    for num in arr:
        n = len(result)
        for i in range(n):
            currSet = list(result[i])
            currSet.append(num)
            key = ','.join(str(e) for e in currSet)
            if exists.get(key) is None:
                exists[key] = 1
                result.append(currSet)
    return result

print(solve([1, 3, 3]))
print(solve([1, 5, 3, 3]))
