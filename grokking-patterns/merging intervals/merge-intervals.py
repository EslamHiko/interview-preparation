'''
Problem Statement #
Given a list of intervals, merge all the overlapping intervals to produce a list that has only mutually exclusive intervals.

Example 1:

Intervals: [[1,4], [2,5], [7,9]]
Output: [[1,5], [7,9]]
Explanation: Since the first two intervals [1,4] and [2,5] overlap, we merged them into
one [1,5].
svg viewer
Example 2:

Intervals: [[6,7], [2,4], [5,9]]
Output: [[2,4], [5,9]]
Explanation: Since the intervals [6,7] and [5,9] overlap, we merged them into one [5,9].

Example 3:

Intervals: [[1,4], [2,6], [3,5]]
Output: [[1,6]]
Explanation: Since all the given intervals overlap, we merged them into one.
'''

def sol(intervals):
    intervals.sort(key=lambda x: x[0])
    start = intervals[0][0]
    end = intervals[0][1]
    merged = [start,end]
    final = []
    for i in range(1,len(intervals)):
        if end >= intervals[i][0]:
            end = max(end,intervals[i][1])
            merged = [start,end]
        else:
            final.append(merged)
            start = intervals[i][0]
            end = intervals[i][1]
    final.append([start,end])
    return final

print(sol([[1,4], [2,5], [7,9]]))
print(sol([[6,7], [2,4], [5,9]]))
print(sol([[1,4], [2,6], [3,5]]))

'''
Problem 1: Given a set of intervals, find out if any two intervals overlap.

Example:

Intervals: [[1,4], [2,5], [7,9]]
Output: true
Explanation: Intervals [1,4] and [2,5] overlap
'''
def sol2(intervals):
    intervals.sort(key=lambda x: x[0])
    start,end = intervals[0][0],intervals[0][1]
    merged = [start,end]
    for i in range(1,len(intervals)):
        if end >= intervals[i][0]:
            return True
        else:
            end = intervals[i][1]

    return False

print(sol2([[1,4], [5,6], [6,9]]))
print(sol2([[1,4], [5,6], [7,9]]))
