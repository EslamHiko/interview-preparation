'''
Problem Statement #
Given a string, sort it based on the decreasing frequency of its characters.

Example 1:

Input: "Programming"
Output: "rrggmmPiano"
Explanation: 'r', 'g', and 'm' appeared twice, so they need to appear before any other character.
Example 2:

Input: "abcbab"
Output: "bbbaac"
Explanation: 'b' appeared three times, 'a' appeared twice, and 'c' appeared only once.
'''
import collections
def solve(string):
    map = {}
    for ch in string:
        map[ch] = map.get(ch,0)+1

    freqs = collections.defaultdict(lambda:[])

    for ch in map.keys():
        freqs[map[ch]].append(ch)

    freqs_keys = list(freqs.keys())
    freqs_keys.sort()

    result = ''
    while len(freqs_keys):
        curr = freqs_keys.pop()
        for ch in freqs[curr]:
            result += ch * curr

    return result

print(solve("Programming"))
print(solve("abcbab"))
