#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'maxShared' function below.
#
# The function is expected to return an INTEGER.
# The function accepts WEIGHTED_INTEGER_GRAPH friends as parameter.
#

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] and <name>_to[i]. The weight of the edge is <name>_weight[i].
#
#
import collections
def maxShared(friends_nodes, friends_from, friends_to, friends_weight):
    # Write your code here
    # the tests' results are wrong ? ? !
    '''
    5 7     # weight  nodes
    1 2 1   #   1       1,[2],3,[4],5
    1 2 2   #   2       1,[2],[4],5
    2 3 1   #   3       [2],3,[4]
    2 3 3
    2 4 3   # the max nodes with interests are (2,4)
    4 5 1       2 : 1,2,3
    4 5 2       4 : 3,2,1
                2 * 4 = 8 How come is the result 20 ?!!!
    '''
    interests = collections.defaultdict(lambda: {})
    graphWeight = collections.defaultdict(lambda: 0)
    for i in range(friends_edges):
        interests[friends_from[i]][friends_weight[i]] = 1
        interests[friends_to[i]][friends_weight[i]] = 1

    count = 0
    maxL = 0
    maxGraphs = collections.defaultdict(lambda: [])
    for i in range(1,friends_nodes+1):
        print(interests[i].keys())
        for j in range(i+1,friends_nodes+1):
            l = len(set(interests[i].keys()).intersection(set(interests[j].keys())))
            maxL = max(l,maxL)
            maxGraphs[l].append((i,j))
    print(maxL)
    print(maxGraphs[maxL])
    print(maxGraphs)
    for pair in maxGraphs[maxL]:
        count = max(count,pair[0]*pair[1])
    return count
