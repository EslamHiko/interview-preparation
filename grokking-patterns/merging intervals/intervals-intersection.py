'''
Problem Statement #
Given two lists of intervals, find the intersection of these two lists. Each list consists of disjoint intervals sorted on their start time.

Example 1:

Input: arr1=[[1, 3], [5, 6], [7, 9]], arr2=[[2, 3], [5, 7]]
Output: [2, 3], [5, 6], [7, 7]
Explanation: The output list contains the common intervals between the two lists.
Example 2:

Input: arr1=[[1, 3], [5, 7], [9, 12]], arr2=[[5, 10]]
Output: [5, 7], [9, 10]
Explanation: The output list contains the common intervals between the two lists.
'''

def sol(arr1,arr2):
    i,j = 0,0
    start,end = 0,1
    final = []
    while i < len(arr1) and j < len(arr2):
        '''
        A => |==========|=========|
        B =>            |================|
        '''
        a_overlabs_b = arr1[i][start] >= arr2[j][start] and arr1[i][start] <= arr2[j][end]
        b_overlabs_a = arr2[j][start] >= arr1[i][start] and arr2[j][start] <= arr1[i][end]

        if a_overlabs_b or b_overlabs_a:
            final.append([max(arr1[i][start],arr2[j][start]),min(arr1[i][end],arr2[j][end])])

        if arr1[i][end] < arr2[j][end]:
            i += 1
        else:
            j += 1

    return final

print(sol([[1, 3], [5, 6], [7, 9]],[[2, 3], [5, 7]]))
print(sol([[1, 3], [5, 7], [9, 12]],[[5, 10]]))
