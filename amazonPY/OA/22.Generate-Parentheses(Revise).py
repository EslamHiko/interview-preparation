'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''
def sol(n):
    def helper(opened,closed,s):
        if opened == n and closed == n:
            res.append(s)
            return
        if opened < n:
            helper(opened + 1,closed,s+"(")
        if opened > closed:
            helper(opened,closed+1,s+")")

    res = []
    helper(0,0,"")

    return res
