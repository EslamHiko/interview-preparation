'''
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
'''
def sol1(nums):
    maxProd = nums[0]
    minProd = nums[0]
    result = nums[0]
    for i in range(1,len(nums)):
        maxProd, minProd = max(maxProd*nums[i],minProd*nums[i],nums[i]), min(maxProd*nums[i],minProd*nums[i],nums[i])
        result = max(result,maxProd)
    return result

def sol2(nums):
    nums2 = nums.copy()
    nums2.reverse()

    for i in range(1,len(nums)):
        nums[i] *= nums[i-1] or 1
        nums2[i] *= nums2[i-1] or 1

    return max(nums+nums2)
