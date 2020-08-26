'''
Problem Statement #
Given an array of characters where each character represents a fruit tree, you are given two baskets and your goal is to put maximum number of fruits in each basket.
The only restriction is that each basket can have only one type of fruit.

You can start with any tree, but once you have started you can’t skip a tree. You will pick one fruit from each tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.

Write a function to return the maximum number of fruits in both the baskets.

Example 1:

Input: Fruit=['A', 'B', 'C', 'A', 'C']
Output: 3
Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']

Example 2:

Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C']
Output: 5

Explanation: We can put 3 'B' in one basket and two 'C' in the other basket.
This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']
'''
import collections

def sol(arr):
    map = collections.defaultdict(lambda: 0)
    start,count = 0,0
    maxCount = float('-inf')
    for end in range(len(arr)):
        map[arr[end]] += 1
        count += 1
        while len(map.keys()) > 2:
            map[arr[start]] -= 1
            if map[arr[start]] == 0:
                del map[arr[start]]
            start += 1
            count -= 1
        maxCount = max(maxCount,count)
    return maxCount

print(sol(['A', 'B', 'C', 'A', 'C']))
print(sol(['A', 'B', 'C', 'B', 'B', 'C']))
