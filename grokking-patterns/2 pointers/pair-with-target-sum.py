'''
Problem Statement #
Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.

Write a function to return the indices of the two numbers (i.e. the pair) such that they add up to the given target.

Example 1:

Input: [1, 2, 3, 4, 6], target=6
Output: [1, 3]
Explanation: The numbers at index 1 and 3 add up to 6: 2+4=6
Example 2:

Input: [2, 5, 9, 11], target=11
Output: [0, 2]
Explanation: The numbers at index 0 and 2 add up to 11: 2+9=11
'''

def sol(arr,sum):
    i = 0
    j = len(arr)-1
    while i < j:
        if arr[i]+arr[j] > sum:
            j -= 1
        if arr[i]+arr[j] < sum:
            i += 1
        if arr[i]+arr[j] == sum and i != j:
            return i,j
    return -1

print(sol([1,2,3,4,6],6))
print(sol([1,3,4,6],6))

def anotherSol(arr,sum):
    needed = {}
    for i in range(len(arr)):
        if needed.get(arr[i]) != None:
            return i,needed[arr[i]]
        needed[sum - arr[i]] = i
    return -1

print(sol([1,2,3,4,6],6))
print(sol([1,3,4,6],6))
