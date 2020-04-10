'''
n a row of dominoes, A[i] and B[i] represent the top and bottom halves of the i-th domino.  (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the i-th domino, so that A[i] and B[i] swap values.

Return the minimum number of rotations so that all the values in A are the same, or all the values in B are the same.

If it cannot be done, return -1.



Example 1:



Input: A = [2,1,2,4,2,2], B = [5,2,6,2,3,2]
Output: 2
Explanation:
The first figure represents the dominoes as given by A and B: before we do any rotations.
If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.
Example 2:

Input: A = [3,5,1,2,3], B = [3,6,3,3,4]
Output: -1
Explanation:
In this case, it is not possible to rotate the dominoes to make one row of values equal.
'''
def sol(A, B):
    mapA = {}
    mapB = {}
    for i in range(len(A)):
        if mapA.get(A[i]):
            mapA[A[i]].append(i)
        else:
            mapA[A[i]] = [i]

        if mapB.get(B[i]):
            mapB[B[i]].append(i)
        else:
            mapB[B[i]] = [i]


    for el in mapA:
        toAppend = mapB.get(el) or []
        fullSet = set(mapA[el]+toAppend)
        if len(fullSet) == len(A):
            return min(len(fullSet-set(mapA[el])),len(fullSet-set(toAppend)))

    return -1

print(sol([2,1,2,4,2,2],[5,2,6,2,3,2]))
print(sol([3,5,1,2,3],[3,6,3,3,4]))
print(sol([1,1,1,1,1],[1,1,1,1,1]))
