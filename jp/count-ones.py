'''
You are given a string with 1's and 0's you need to return the number of changes needed so that you have x number of 1's before 0's where 0<=x<=length of string

Example:
1010
Answer
1
Explanation
convert the 2nd zero to 1 to get 1110, or the 3rd 1 to 0 to get 1000

It must be in O(n)

Any Suggestions ?
'''
def count_ones(s):
    s = str(s)
    max_count = 0
    count = 0
    for i in s:
        if i == "1":
            count += 1
        elif i == "0" and max_count < count:
            max_count = count
            count = 0
        elif i == "0" and max_count >= count:
            count = 0
        else:
            return "Invalid number"

    return max_count

import sys

def minFlips(bits):
    n = len(bits)
    flipsLeft, flipsLeftArray = 0, [0 for i in range(n)]
    flipsRight, flipsRightArray = 0, [0 for i in range(n)]
    minFlips = sys.maxsize

    for i in range(0,n,1):
        if bits[i] == "0":
            flipsLeft += 1
        flipsLeftArray[i] = flipsLeft

    for i in range(n-1,0,-1):
        if bits[i] == "1":
            flipsRight += 1
        flipsRightArray[i] = flipsRight

    for i in range (1,n,1):
        minFlips = min(minFlips, flipsLeftArray[i-1] + flipsRightArray[i])

    return minFlips
    
