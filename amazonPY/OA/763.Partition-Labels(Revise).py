'''
A string S of lowercase letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

Example 1:
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
Note:

S will have length in range [1, 500].
S will consist of lowercase letters ('a' to 'z') only.
'''

def sol(S):
    rst, l = [], len(S)
    dt = {S[i]:i for i in range(l)}
    pre = cur = 0
    for i in range(l):
        cur = max(cur, dt[S[i]])
        if i == cur: 
            rst.append(cur - pre + 1)
            pre = cur + 1
    return rst
