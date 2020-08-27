'''
Problem Statement #
Given an unsorted array of numbers, find the top ‘K’ frequently occurring numbers in it.

Example 1:

Input: [1, 3, 5, 12, 11, 12, 11], K = 2
Output: [12, 11]
Explanation: Both '11' and '12' apeared twice.
Example 2:

Input: [5, 12, 11, 3, 11], K = 2
Output: [11, 5] or [11, 12] or [11, 3]
Explanation: Only '11' appeared twice, all other numbers appeared once.
'''
import collections
from heapq import *
def sol(arr,k):
    numFreqs = collections.defaultdict(lambda: 0)
    for n in arr:
        numFreqs[n] += 1

    freqsNums = collections.defaultdict(lambda: [])
    maxHeap = []
    for n in numFreqs.keys():
        freqsNums[numFreqs[n]].append(n)
        heappush(maxHeap,-numFreqs[n])

    i = 0
    result = []
    while len(maxHeap) and i < k:
        currNums = freqsNums[-heappop(maxHeap)]
        for el in currNums:
            result.append(el)
            i += 1
            if i == k:
                break
    return result

print(sol([5, 12, 11, 3, 11],2))
print(sol([1, 3, 5, 12, 11, 12, 11],2))
