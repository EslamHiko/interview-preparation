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
def sol(strs):
    def isAnagram(string, anagram):
        for char in string:
            if not anagram.get(char):
                return False
            else:
                anagram[char] -= 1
        for el in anagram:
            if anagram[el] >= 1:
                return False
        return True

    def createAnagram(string):
        anagram = {}
        for char in string:
            if anagram.get(char):
                anagram[char] += 1
            else:
                anagram[char] = 1
        return anagram

    allAnagrams = []
    finalAnagrams = {}
    for singleStr in strs:
        foundAnagram = False
        for i in range(len(allAnagrams)):
            if isAnagram(singleStr,allAnagrams[i].copy()):
                finalAnagrams[i].append(singleStr)
                foundAnagram = True

        if not foundAnagram:
            newAnagram = createAnagram(singleStr)
            allAnagrams.append(newAnagram)
            finalAnagrams[len(allAnagrams)-1] = [singleStr]

    finalArr = []
    for el in finalAnagrams:
        finalArr.append(finalAnagrams[el])
    return finalArr

def sol2(strs):
    ans = {}
    for s in strs:
        sortedStr = ''.join(sorted(s))
        if ans.get(sortedStr):
            ans[sortedStr].append(s)
        else:
            ans[sortedStr] = [s]
    return list(ans.values())

print(sol(["eat","tea","tan","ate","nat","bat"]))
print(sol2(["eat","tea","tan","ate","nat","bat"]))
