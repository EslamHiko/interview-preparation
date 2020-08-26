'''
Given a NxN matrix. Fill the integers from 1 to n*n to this matrix that makes the sum of each row, each column and the two diagonals equal.

Example 1:

Input: n = 2
Output: null
Explanation: We need to fill [1, 2, 3, 4] into a 2x2 matrix, which is not possible so return null.
Example 2:

Input: n = 3
Output:
[[8, 3, 4],
 [1, 5, 9],
 [6, 7, 2]]
Explanation: We need to fill [1, 2, 3... 9] into a 3x3 matrix. This is one way to do it
Each row [8, 3, 4] [1, 5, 9] [6, 7, 2] sum is 15.
Each column [8, 1, 6] [3, 5, 7] [4, 9, 2] sum is 15.
The two diagonals [8, 5, 2] [4, 5, 6] sum is 15.
int[][] fillMatrix(int n) {
}
'''
def myrow(pos, n):
    # Returns a list of indices of all elements in the row containing position
    output = []
    pos = pos % n
    return list(range(pos,n**2,n))

def mycol(pos, n):
    # Returns a list of indices of all elements in the column containing position
    output = []
    pos = (pos // n)*n
    return list(range(pos, pos +n))

def top_diagonal(n):
    # Returns a list of indices of all elements in the top left to bottom right diagonal
    return [i*n + i for i in range(n)]

def other_diagonal(n):
    # Returns a list of indices of all elements in top right to bottom left diagonal
    return [i*n + n - i - 1 for i in range(n)]

def issafe(board, pos, x, n):
    # Returns True if x can be placed on the board
    global global_sum
    if(board[pos] is not None):
        return False
    if(x in board):
        return False
    if(pos == myrow(pos, n)[-1]):
        if(x + sum([board[r] for r in myrow(pos, n)[:-1]]) != global_sum):
            return False
    if(pos == mycol(pos, n)[-1]):
        if(x + sum([board[r] for r in mycol(pos, n)[:-1]]) != global_sum):
            return False
    if(pos == top_diagonal(n)[-1]):
        if(x + sum([board[r] for r in top_diagonal(n)[:-1]]) != global_sum):
            return False
    if(pos == other_diagonal(n)[-1]):
        if(x + sum([board[r] for r in other_diagonal(n)[:-1]]) != global_sum):
            return False
    return True

def fill(board, pos, n):
    #Backtracking through the board
    if(pos >= n**2):
        return True
    for num in range(1, n**2+1):
        if(issafe(board, pos, num, n)):
            board[pos] = num
            if(fill(board, pos+1, n)):
                return True
            else:
                board[pos] = None
    return False

n = 3
global_sum = n*(n**2+1)/2
board = [None]*(n**2)
val = fill(board, 0, n)
output = []
for i in range(n):
    output.append(board[i*n:i*n+n])
print(output)
print(val)
