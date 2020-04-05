'''
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
'''
def sol(s,t):
    charMap = {}
    if len(s) > len(t):
        s,t = t,s
    for i in s:
        if charMap.get(i):
            charMap[i] += 1
        else:
            charMap[i] = 1
    for i in t:
        if not charMap.get(i):
            return False
        else:
            charMap[i] -= 1
    return True

print(sol("anagram","nagaram"))
print(sol("rat","car"))
