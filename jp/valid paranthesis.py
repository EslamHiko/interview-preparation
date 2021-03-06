
'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
Example 4:

Input: s = "([)]"
Output: false
Example 5:

Input: s = "{[]}"
Output: true


Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
'''

class Solution:
    def isValid(self, s: str) -> bool:
        charMap = []

        for i in s:
            if len(charMap):
                if i == ')':
                    if charMap[-1] != '(':
                        return False
                    else:
                        charMap.pop()
                elif i == '}':
                    if charMap[-1] != '{':
                        return False
                    else:
                        charMap.pop()
                elif i == ']':
                    if charMap[-1] != '[':
                        return False
                    else:
                        charMap.pop()
                else:
                    charMap.append(i)
            else:
                charMap.append(i)
        return not len(charMap)
