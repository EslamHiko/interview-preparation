'''
Technical phone screen (45 min):
You are given an array A of distinct integers, you have to return another array B which transforms the first array such that the minimum element in the new array is 1 and all the other elements maintain their relative ordering i.e. if A[i] > A[j] then it should also be that B[i] > B[j] and similarly for other elements. Also, the maximum number in B should be minimized. Better explanation of this question can be found here.

Input: [4, 2, 3, 7]
Output: [3, 1, 2, 4]

Input: [-4, -2, -3, -7]
Output: [2, 4, 3, 1]
Follow ups:

What if the elements are not distinct?
Second question: You have to perform the same operation on a 2D array of distinct elements. The ranking should hold for within each row and each column only.
What if the matrix has duplicates?
Input:
1 5 6
4 3 2
8 7 9

Output:
1 3 4
3 2 1
5 4 6
'''

def sol(arr):
    counter = 1
    map = {}
    arrCopy = arr.copy()
    arrCopy.sort()
    for el in arrCopy:
        map[el] = counter
        counter += 1
    for i in range(len(arr)):
        arr[i] = map[arr[i]]
    return arr


print(sol([4, 2, 3, 7]))

print(sol([-4, -2, -3, -7]))

print(sol([-4, -2, -3, -3, -7]))

'''
if elements are distinct they will be incremented
for example 2,2,3
will be 1,2,3
in case we can want it 1,1
we can add a simple check in our code and set it to the same counter value without incrementing it
'''

def sol2(arr):
    counter = 1
    map = {}
    arrCopy = arr.copy()
    arrCopy.sort()
    for el in arrCopy:
        if not map.get(el):
            map[el] = counter
            counter += 1
    for i in range(len(arr)):
        arr[i] = map[arr[i]]
    return arr

print(sol2([4, 2, 2,3, 7]))

print(sol2([-4, -2, -3,-3, -7]))

def sol2D(arr2d):
    arr = []
    map = {}
    for el in arr2d:
        for el2 in el:
            arr.append(el2)
    arr.sort()
    for el in arr:
        if not map.get(el):
            map[el] = counter
            counter += 1
    for i in range(len(arr2d)):
        for j in range(len(i)):
            arr2d[i][j] = map[arr2d[i][j]]
    return arr2d
