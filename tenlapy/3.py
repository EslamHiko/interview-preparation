#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getMinimumDifference' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY a
#  2. STRING_ARRAY b
#

def getMinimumDifference(a, b):
    # Write your code here
    result = []
    for i in range(len(a)):
        if len(a[i]) != len(b[i]):
            result.append(-1)
        else:
            map = {}
            count = 0
            for c in a[i]:
                if map.get(c) is not None:
                    map[c] += 1
                else:
                    map[c] = 1
            for c in b[i]:
                if map.get(c):
                    map[c] -= 1
                else:
                    count += 1
            result.append(count)
    return result
