'''
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for string in strs:
            copy = string
            copy = list(copy)
            copy.sort()
            if map.get(tuple(copy)):
                map[tuple(copy)].append(string)
            else:
                map[tuple(copy)] = [string]
        return map.values()
