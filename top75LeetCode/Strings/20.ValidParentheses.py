'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
'''
def sol(s):
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


print(sol("()"))
print(sol("()[]{}"))
print(sol("([)]"))
print(sol("(]"))
print(sol("{[]}"))
