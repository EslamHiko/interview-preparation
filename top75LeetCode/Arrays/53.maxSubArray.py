'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
'''

def sol(nums):
    length = len(nums)
    dp = [0]*length
    answer = nums[0]
    for i in range(1,length):
        dp[i] = max(dp[i-1]+nums[i],nums[i])
        answer = max(dp[i],answer)
    return answer

def solOptimized1(nums):
    length = len(nums)
    curr_max = arr[0]
    answer = nums[0]
    for i in range(1,length):
        curr_max = max(curr_max+nums[i],nums[i])
        answer = max(curr_max,answer)
    return answer

def solOptimized2(nums):
      max_sum = nums[0]
    for i in range(1,len(nums)):
        nums[i] = max(nums[i-1]+nums[i],nums[i])
        max_sum = max(nums[i],max_sum)
    return max_sum
