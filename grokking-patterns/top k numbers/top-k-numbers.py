'''
Problem Statement #
Given an unsorted array of numbers, find the ‘K’ largest numbers in it.

Note: For a detailed discussion about different approaches to solve this problem, take a look at Kth Smallest Number.

Example 1:

Input: [3, 1, 5, 12, 2, 11], K = 3
Output: [5, 12, 11]
Example 2:

Input: [5, 12, 11, -1, 12], K = 3
Output: [12, 11, 12]
'''
from heapq import *

def solve(arr,k):
    minHeap = []
    for el in arr:
        heappush(minHeap,-1*el)

    result = []
    for i in range(k):
        result.append(-1*heappop(minHeap))

    return result

def solve2(arr,k):
    minHeap = []
    for el in arr:
        heappush(minHeap,el)

    result = []
    for i in range(k):
        result.append(heappop(minHeap))

    return result
    
print(solve([3, 1, 5, 12, 2, 11],3))
print(solve2([3, 1, 5, 12, 2, 11],3))

print(solve([5, 12, 11, -1, 12],3))
print(solve2([5, 12, 11, -1, 12],3))
