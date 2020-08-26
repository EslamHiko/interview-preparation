'''
Problem Statement #
Given a string with lowercase letters only, if you are allowed to replace no more than ‘k’ letters with any letter, find the length of the longest substring having the same letters after replacement.

Example 1:

Input: String="aabccbb", k=2
Output: 5

Explanation: Replace the two 'c' with 'b' to have a longest repeating substring "bbbbb".
Example 2:

Input: String="abbcb", k=1
Output: 4

Explanation: Replace the 'c' with 'b' to have a longest repeating substring "bbbb".
Example 3:

Input: String="abccde", k=1
Output: 3

Explanation: Replace the 'b' or 'd' with 'c' to have the longest repeating substring "ccc".
'''
import collections
def sol(s,k):
    start = 0
    maxCount = 0
    maxChar = s[0]
    maxCharCount = 0
    couldBeReplaced = 0
    map = collections.defaultdict(lambda: 0)
    for end in range(len(s)):
        map[s[end]] += 1
        if maxCharCount < map[s[end]]:
            maxCharCount = map[s[end]]
            maxChar = s[end]
        if s[end] != maxChar:
            couldBeReplaced += 1
        while couldBeReplaced > k:
            map[s[start]] -= 1
            if map[s[start]] == 0:
                del map[s[start]]
            start += 1
            couldBeReplaced -= 1
    return maxCharCount + couldBeReplaced

print(sol("aabccbb",2))

print(sol("abbcb",1))
print(sol("abccde",1))

print(sol("abcbb",3))

def anotherSol(s,k):
    start,maxLength,maxRepeatChar = 0,0,0
    map = {}
    for end in range(len(s)):
        right_char = s[end]
        if right_char not in map:
            map[right_char] = 0
        map[right_char] += 1
        maxRepeatChar = max(maxRepeatChar,map[right_char])
        chars_other_than_max_repeat_char_count = end - start + 1 - maxRepeatChar
        if  chars_other_than_max_repeat_char_count > k:
            left_char = s[start]
            map[left_char] -= 1
            start += 1
        maxLength = max(maxLength,end-start+1)
    return maxLength

print(anotherSol("aabccbb",2))

print(anotherSol("abbcb",1))
print(anotherSol("abccde",1))

print(anotherSol("abcbb",3))
