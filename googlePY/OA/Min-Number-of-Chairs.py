'''
There are n guests who are invited to a party. The k-th guest will attend the party at time S[k] and leave the party at time E[k].

Given an integer array S and an integer array E, both of length n, return an integer denoting the minimum number of chairs you need such that everyone attending the party can sit down.

Example:

Input: S = [1, 2, 6, 5, 3], E = [5, 5, 7, 6, 8]
Output: 3
Explanation:
There are five guests attending the party.
The 1st guest will arrive at time 1. We need one chair at time 1.
The 2nd guest will arrive at time 2. There are now two guests at the party, so we need two chairs at time 2.
The 5th guest will arrive at time 3. There are now three guests at the party, so we need three chairs at time 3.
The 4th guest will arrive at time 5 and, at the same moment, the 1st and 2nd guests will leave the party.
There are now two (the 4th and 5th) guests at the party, so we need two chairs at time 5.
The 3rd guest will arrive at time 6, and the 4th guest will leave the party at the same time.
There are now two (the 3rd and 5th) guests at the party, so we need two chairs at time 6.
So we need at least 3 chairs.
Related problems:

https://leetcode.com/problems/meeting-rooms-ii (premium)
'''
def sol(start,end):
    all = [(s,1) for s in start] + [(e,-1) for e in end]
    all.sort()
    curr = 0
    minChairs = 0
    for s, t in all:
        curr += t
        minChairs = max(minChairs,curr)
    return minChairs

print(sol([1, 2, 6, 5, 3],[5, 5, 7, 6, 8]))

# more optimized
def sol2(start,end):
    maxStart = max(start)
    maxEnd = max(end)
    maxAll = max(maxStart,maxEnd)
    availabilitySlotsPerHour = [0]*(maxAll+2)
    for i in range(len(start)):
        availabilitySlotsPerHour[start[i]] += 1
        availabilitySlotsPerHour[end[i]] -= 1

    maxMinChairs = -1
    curr = 0
    for i in range(len(availabilitySlotsPerHour)):
        curr += availabilitySlotsPerHour[i]
        maxMinChairs = max(maxMinChairs,curr)

    return maxMinChairs

print(sol2([1, 2, 6, 5, 3],[5, 5, 7, 6, 8]))
