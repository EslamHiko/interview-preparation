'''
Given a string s and an int k, return an int representing the number of substrings (not unique) of s with exactly k distinct characters. If the given string doesn't have k distinct characters, return 0.
https://leetcode.com/problems/subarrays-with-k-different-integers

Example 1:

Input: s = "pqpqs", k = 2
Output: 7
Explanation: ["pq", "pqp", "pqpq", "qp", "qpq", "pq", "qs"]
Example 2:

Input: s = "aabab", k = 3
Output: 0
Constraints:

The input string consists of only lowercase English letters [a-z]
0 ≤ k ≤ 26
'''

def sol(str,k):
    count = 0
    for i in range(len(str)):
        for j in range(i+k,len(str)+1):
            newStr = str[i:j]
            if len(set(list(newStr))) == k:
                count += 1
    return count

print(sol("pqpqs",2))
print(sol("aabab",3))

'''
Given a string s and an int k, return all unique substrings of s of size k with k distinct characters.

Example 1:

Input: s = "abcabc", k = 3
Output: ["abc", "bca", "cab"]
Example 2:

Input: s = "abacab", k = 3
Output: ["bac", "cab"]
Example 3:

Input: s = "awaglknagawunagwkwagl", k = 4
Output: ["wagl", "aglk", "glkn", "lkna", "knag", "gawu", "awun", "wuna", "unag", "nagw", "agwk", "kwag"]
Explanation:
Substrings in order are: "wagl", "aglk", "glkn", "lkna", "knag", "gawu", "awun", "wuna", "unag", "nagw", "agwk", "kwag", "wagl"
"wagl" is repeated twice, but is included in the output once.
Constraints:

The input string consists of only lowercase English letters [a-z]
0 ≤ k ≤ 26
Solution
Java sliding window: https://leetcode.com/playground/LRBxfw5W
'''
def sol2(str,k):
    sols = []
    for i in range(len(str)):
        for j in range(i+k,len(str)+1):
            newStr = str[i:j]
            if len(set(list(newStr))) == k and len(newStr) == k:
                sols.append(newStr)
    return set(sols)

print(sol2("abcabc",3))
print(sol2("abacab",3))

print(sol2("awaglknagawunagwkwagl",4))
