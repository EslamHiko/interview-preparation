'''
Problem Statement #
Given an array of intervals representing ‘N’ appointments, find out if a person can attend all the appointments.

Example 1:

Appointments: [[1,4], [2,5], [7,9]]
Output: false
Explanation: Since [1,4] and [2,5] overlap, a person cannot attend both of these appointments.
Example 2:

Appointments: [[6,7], [2,4], [8,12]]
Output: true
Explanation: None of the appointments overlap, therefore a person can attend all of them.
Example 3:

Appointments: [[4,5], [2,3], [3,6]]
Output: false
Explanation: Since [4,5] and [3,6] overlap, a person cannot attend both of these appointments.

'''

def sol(arr):
    # ask if it's sorted
    arr.sort(key=lambda x: x[0])

    i = 1
    start,end = 0,1

    while i < len(arr):
        if arr[i-1][end] > arr[i][start]:
            return False
        i += 1
    return True

print(sol([[1,4], [2,5], [7,9]]))
print(sol([[6,7], [2,4], [8,12]]))
print(sol([[4,5], [2,3], [3,6]]))

'''
Similar Problems #
Problem 1: Given a list of appointments, find all the conflicting appointments.

Example:

Appointments: [[4,5], [2,3], [3,6], [5,7], [7,8]]
Output:
[4,5] and [3,6] conflict.
[3,6] and [5,7] conflict.

'''
def sol2(arr):
    # ask if it's sorted
    arr.sort(key=lambda x: x[0])

    curr = 0
    toCompareWith = 1
    start,end = 0,1
    conflicts = []

    print(arr)
    while curr < len(arr)-1:
        if arr[curr][end] > arr[toCompareWith][start]:
            conflicts.append([arr[curr],arr[toCompareWith]])
            toCompareWith = toCompareWith+1
        else:
            curr += 1
            toCompareWith = curr+1


    return conflicts

print(sol2([[4,5], [2,3], [3,6], [5,7], [7,8]]))
