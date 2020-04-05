'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
'''
def sol(nums):
    reverse = False
    if not len(nums):
        return -1
    if target > nums[-1]:
        nums.reverse()
        reverse = True
    length = len(nums)
    for i in range(1,length+1):
        if target == nums[length - i]:
            return i-1 if reverse else length-i
    return -1
