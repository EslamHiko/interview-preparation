'''
Problem Statement #
Given a string, find the length of the longest substring which has no repeating characters.

Example 1:

Input: String="aabccbb"
Output: 3
Explanation: The longest substring without any repeating characters is "abc".
Example 2:

Input: String="abbbb"
Output: 2
Explanation: The longest substring without any repeating characters is "ab".
Example 3:

Input: String="abccde"
Output: 3
Explanation: Longest substrings without any repeating characters are "abc" & "cde".
'''
import collections
def sol(s):
    start,count = 0,0
    map = collections.defaultdict(lambda: 0)
    maxCount = float('-inf')
    maxCountStarts = collections.defaultdict(lambda: [])
    for end in range(len(s)):
        map[s[end]] += 1
        count += 1
        while map[s[end]] > 1:
            count -= 1
            map[s[start]] -= 1
            if map[s[start]] == 0:
                del map[s[start]]
            start += 1
        if maxCount <= count:
            maxCount = count
            maxCountStarts[maxCount].append(start)
    return maxCount,[s[startIndex:startIndex+maxCount] for startIndex in maxCountStarts[maxCount]]

print(sol("aabccbb"))
print(sol("abbbb"))
print(sol("abccde"))

def anotherSol(s):
    start,maxLength = 0,0
    charMap = {}
    for end in range(len(s)):
        right_char =  s[end]
        if right_char in charMap:
            start =  max(start,charMap[r]+1)
        charMap[right_char] = end
        maxLength = max(maxLength,end-start+1)
    return maxLength

print(anotherSol("aabccbb"))
print(anotherSol("abbbb"))
print(anotherSol("abccde"))
