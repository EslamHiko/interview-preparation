'''
Problem Statement #
Given an array of positive numbers and a positive number ‘k’, find the maximum sum of any contiguous subarray of size ‘k’.

Example 1:

Input: [2, 1, 5, 1, 3, 2], k=3
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].
Example 2:

Input: [2, 3, 4, 1, 5], k=2
Output: 7
Explanation: Subarray with maximum sum is [3, 4].
'''

def sol(arr,k):
    sum,start = 0,0
    maxSum = float('-inf')
    for end in range(len(arr)):
        sum += arr[end]
        if end >= k-1:
            maxSum = max(maxSum,sum)
            sum -= arr[start]
            start += 1
    return maxSum

print(sol([2, 1, 5, 1, 3, 2],3))
print(sol([2, 3, 4, 1, 5],2))
