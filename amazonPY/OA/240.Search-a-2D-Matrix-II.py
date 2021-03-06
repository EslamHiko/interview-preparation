'''
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
Example:

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.
'''
def sol(matrix,target):
    if not len(matrix) or not len(matrix[0]):
        return False

    row,col = 0,len(matrix[0])-1
    length = len(matrix)

    while row <= length-1 and col >= 0:
        if matrix[row][col] == target:
            return True

        if target > matrix[row][col]:
            row += 1
        else:
            col -= 1

    return False
