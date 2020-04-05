'''
Given an int array nums and an int target, find how many unique pairs in the array such that their sum is equal to target. Return the number of pairs.

Example 1:

Input: nums = [1, 1, 2, 45, 46, 46], target = 47
Output: 2
Explanation:
1 + 46 = 47
2 + 45 = 47
Example 2:

Input: nums = [1, 1], target = 2
Output: 1
Explanation:
1 + 1 = 2
Example 3:

Input: nums = [1, 5, 1, 5], target = 6
Output: 1
Explanation:
[1, 5] and [5, 1] are considered the same.
Related problems:

https://leetcode.com/problems/two-sum
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted
'''
def mySol(arr,target):
    missing = {}
    results = {}
    for i in arr:
        if missing.get(i) is not None:
            if missing[i] > i:
                results[(i,missing[i])] = 1
            else:
                results[(missing[i],i)] = 1
        missing[target-i] = i
    return len(results.keys())

print(mySol([1, 1, 2, 45, 46, 46],47))

print(mySol([1, 1],2))

print(mySol([1, 5, 1, 5],6))

'''
1. Two Sum

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

def sol1(nums,target):
    missing = {}
    indices = {}
    for i in range(len(nums)):
        if missing.get(nums[i]) is not None :
            return [i,indices[missing[nums[i]]]]
        missing[target-nums[i]] = nums[i]
        indices[nums[i]] = i

'''
167. Two Sum II - Input array is sorted

Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
Example:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
'''
def sol167(numbers,target):
    index1 = 0
    index2 = len(numbers)-1
    while index1 < index2:
        if numbers[index1] + numbers[index2] == target:
            return [index1+1,index2+1]
        elif numbers[index1] + numbers[index2] > target:
            index2 -= 1
        else:
            index1 += 1

    return []

'''
653. Two Sum IV - Input is a BST

Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

Example 1:

Input:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

Output: True


Example 2:

Input:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

Output: False
'''
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

def sol653(root,target):
    missing = {}
    def traverse(root):
        if root:
            if missing.get(root.val) is not None:
                return True
            missing[k-root.val] = root.val
            return traverse(root.right) or traverse(root.left)
    return traverse(root)

'''
Given a list of positive integers nums and an int target, return indices of the two numbers such that they add up to a target - 30.

Conditions:

You will pick exactly 2 numbers.
You cannot pick the same element twice.
If you have muliple pairs, select the pair with the largest number.
Example 1:

Input: nums = [1, 10, 25, 35, 60], target = 90
Output: [2, 3]
Explanation:
nums[2] + nums[3] = 25 + 35 = 60 = 90 - 30
Example 2:

Input: nums = [20, 50, 40, 25, 30, 10], target = 90
Output: [1, 5]
Explanation:
nums[0] + nums[2] = 20 + 40 = 60 = 90 - 30
nums[1] + nums[5] = 50 + 10 = 60 = 90 - 30
You should return the pair with the largest number.
Solution
Related problems:

https://leetcode.com/problems/two-sum
'''
def solGivenSum(nums,target):
    missing = {}
    indices = {}
    results = []
    target -= 30
    for i in range(len(nums)):
        if missing.get(nums[i]) is not None :
            results.append([nums[i],missing[nums[i]]])
        missing[target-nums[i]] = nums[i]
        indices[nums[i]] = i
    results.sort(key=lambda x: (x[0],x[1]))
    if not len(results):
        return None
    return [indices[results[0][0]],indices[results[0][1]]]

print(solGivenSum([1, 10, 25, 35, 60],90))

print(solGivenSum([20, 50, 40, 25, 30, 10],90))
