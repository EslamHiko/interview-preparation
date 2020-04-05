'''
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?
'''
def sol(arr):
    n =  len(nums)
    dp = [0]*n
    res = min(1,n)
    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j])

        dp[i] += 1
        res = max(res,dp[i])

    return res

def sol2(arr):
    dp = [float('inf') for _ in range(len(nums) + 1)]
    for num in nums:
        dp[bisect.bisect_left(dp, num)] = num
    return dp.index(float('inf'))
