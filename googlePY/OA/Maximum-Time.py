'''
ref: https://leetcode.com/discuss/interview-question/396769/
You are given a string that represents time in the format hh:mm. Some of the digits are blank (represented by ?). Fill in ? such that the time represented by this string is the maximum possible. Maximum time: 23:59, minimum time: 00:00. You can assume that input string is always valid.

Example 1:

Input: "?4:5?"
Output: "14:59"
Example 2:

Input: "23:5?"
Output: "23:59"
Example 3:

Input: "2?:22"
Output: "23:22"
Example 4:

Input: "0?:??"
Output: "09:59"
Example 5:

Input: "??:??"
Output: "23:59"
'''
def sol(string):
    finalStr = ''
    maxRanges = {
    0:(1 if string[1] != '?' and int(string[1]) > 3 else 2),
    1: 9,
    2:':',
    3:5,
    4:9}
    for i in range(len(string)):
        if i == 1 and string[i] == '?' and finalStr[0] == '2':
            finalStr += '3'
        else:
            finalStr += str(maxRanges[i]) if string[i] == '?' else string[i]
    return finalStr

print(sol("?4:5?"))
print(sol("23:5?"))
print(sol("2?:22"))
print(sol("1?:?2"))
print(sol("2?:?2"))
print(sol("??:??"))
print(sol("23:5?"))# 23:59
print(sol("2?:22"))# 23:22
print(sol("0?:??"))# 09:59
print(sol("1?:??"))# 19:59
print(sol("?4:??"))# 14:59
print(sol("?3:??"))# 23:59
print(sol("??:??"))# 23:59
print(sol("?4:5?"))#14:59
print(sol("?4:??"))#14:59
print(sol("?3:??"))#23:59
print(sol("23:5?"))#23:59
print(sol("2?:22"))#23:22
print(sol("0?:??"))#09:59
print(sol("1?:??"))#19:59
print(sol("?4:0?"))#14:09
print(sol("?9:4?"))
