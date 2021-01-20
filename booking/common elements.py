'''
Three integer arrays are given with duplicate numbers. Find the common elements among three arrays.
'''
import collections
def sol(arrs):
    hm = collections.defaultdict(lambda: 0)
    for arr in arrs:
        for el in arr:
            hm[el] += 1
    result =  []
    for i in hm.keys():
        if hm[i] >= 3:
            result.append(i)

    return result
