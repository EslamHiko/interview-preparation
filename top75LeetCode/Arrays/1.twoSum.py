'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

def sol(nums,target):
    missing = {}
    indices = {}
    for i in range(len(nums)):
        if missing.get(nums[i]) is not None:
            return [i,indices[missing[nums[i]]]],[nums[i],missing[nums[i]]] # the indices, the numbers
        missing[target-nums[i]] = nums[i]
        indices[nums[i]] = i

print(sol([2, 7, 11, 15],9))
print(sol([0,4,3,0],0))
