'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
'''

# brute force with memorization
def sol(s):
    def isPalindrome(s,memo):
        if memo.get(s) == 0:
            return False
        elif memo.get(s) == 1:
            return True

        for i in range(len(s)):
            j = len(s)-1-i
            if s[i] != s[j]:
                memo[s] = 0
                return False
        memo[s] = 1
        return True

    maxLen = 0
    palindromes = {}
    memo = {}
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            string = s[i:j]
            if isPalindrome(string,memo):
                length = len(string)
                if length > maxLen:
                    maxLen = length
                if palindromes.get(length):
                    palindromes[length].append(string)
                else:
                    palindromes[length] = [string]
    if palindromes.get(maxLen):
        return palindromes[maxLen][0]
    return ""

def expandFromMiddle(s):
    def expandM(s,l,r,length):
        while (l >= 0) and (r < length) and (s[l] == s[r]):
            l -= 1
            r += 1

        return r-l-1,l+1

    length = len(s)
    maxLen = 0
    maxPalindromes = {0:""}

    for i in range(length):
        len1,index1 = expandM(s,i,i,length)
        len2,index2 = expandM(s,i,i+1,length)
        maxLen = max(maxLen,len1,len2)
        if maxPalindromes.get(maxLen) is None:
            maxPalindromes[maxLen] = s[index1:index1+maxLen] if maxLen == len1 else s[index2:index2+maxLen]


    return maxPalindromes[maxLen]
