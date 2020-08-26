#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'strokesRequired' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY picture as parameter.
#
import collections
def strokesRequired(picture):
    # Write your code here
    # it's strange to pass all tests except the last one I think there's a bug with the compiler
    count = 0
    visited = collections.defaultdict(lambda: False)
    def color(visited,i,j,picture,curr):
        # right
        if i < 0 or i > len(picture)-1 or j < 0 or j > len(picture[i])-1:
            return
        if visited[(i,j)]:
            return
        if picture[i][j] == curr:
            visited[(i,j)] = 1
            if j+1 <= len(picture[i])-1:
                if picture[i][j+1] == curr and not visited[(i,j+1)]:
                    color(visited,i,j+1,picture,curr)
            if j-1 >= 0:
                if picture[i][j-1] == curr and not visited[(i,j-1)]:
                    color(visited,i,j-1,picture,curr)
            if i+1 <= len(picture)-1:
                if picture[i+1][j] == curr and not visited[(i+1,j)]:
                    color(visited,i+1,j,picture,curr)
            if i-1 >= 0:
                if picture[i-1][j] == curr and not visited[(i-1,j)]:
                    color(visited,i-1,j,picture,curr)
        else:
            return
    for i in range(len(picture)):
        for j in range(len(picture[i])):
            if not visited[(i,j)]:
                count += 1
                curr = picture[i][j]
                color(visited,i,j,picture,curr)
    return count
