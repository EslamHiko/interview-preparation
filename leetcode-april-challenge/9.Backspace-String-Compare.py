'''
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".
Note:

1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.
Follow up:

Can you solve it in O(N) time and O(1) space?
'''
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def removeBacks(string):
            i = 0
            string = list(string)
            while i < len(string):
                if string[i] == '#':
                    del string[i]
                    if i - 1 >= 0:
                        del string[i-1]
                        i -= 1
                    continue
                i += 1
            return ''.join(string)

        return removeBacks(S) == removeBacks(T)
