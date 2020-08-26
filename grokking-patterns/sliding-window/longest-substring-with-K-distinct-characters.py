'''
Problem Statement #
Given a string, find the length of the longest substring in it with no more than K distinct characters.

Example 1:

Input: String="araaci", K=2
Output: 4

Explanation: The longest substring with no more than '2' distinct characters is "araa".
Example 2:

Input: String="araaci", K=1
Output: 2

Explanation: The longest substring with no more than '1' distinct characters is "aa".
Example 3:

Input: String="cbbebi", K=3
Output: 5

Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".
'''
import collections

def sol(s,k):
    start = 0
    map = collections.defaultdict(lambda: 0)
    maxCount = float('-inf')
    count = 0
    for end in range(len(s)):
        map[s[end]] += 1
        count += 1
        while len(map.keys()) > k:
            map[s[start]] -= 1
            if map[s[start]] == 0:
                del map[s[start]]
            start += 1
            count -= 1
        maxCount = max(maxCount,count)
    return maxCount
print(sol("araaci",2))
print(sol("araaci",1))
print(sol("cbbebi",3))
