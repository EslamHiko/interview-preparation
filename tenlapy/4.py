#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'minSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY num
#  2. INTEGER k
#
import collections
from heapq import heappop, heappush, heapify
def minSum(num, k):
    # Write your code here
    '''
    map = collections.defaultdict(lambda: [])
    for i in range(len(num)):
        map[num[i]].append(i)
    while k > 0:
        maxNum = max(num)
        if maxNum == 1:
            break
        if map.get(maxNum):
            index = map[maxNum].pop()
            num[index] = math.ceil(num[index]/2)
            map[num[index]].append(index)

        k -= 1


    return sum(num)
    '''
    heap = []
    for el in num:
        heappush(heap,-1*el)
    while k > 0:
        maxNum = heap[0]
        if maxNum == -1:
            break
        maxNum = heappop(heap)
        newEl = math.floor(maxNum/2)
        heappush(heap, newEl)

        k -= 1
    return -1*sum(heap)
