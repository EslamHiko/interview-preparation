'''
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
'''

def sol(nums):
    length = len(nums)
    answer = [0]*length

    answer[0] = 1
    for i in range(1,length):
        answer[i] = nums[i-1]*answer[i-1]
        print(answer)

    R = 1
    print(answer)
    for i in reversed(range(length)):
        answer[i] = answer[i] * R
        print(answer)
        R *= nums[i]

    return answer

print(sol([1,2,3,4]))
