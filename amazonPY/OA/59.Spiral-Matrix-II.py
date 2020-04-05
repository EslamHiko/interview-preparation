'''
Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
'''

def sol(n):
    visited = {}
    curr = 'right'

    res = []
    for i in range(n):
        res.append([0]*n)

    i = 0
    j = -1
    count = 0



    while count <= (n*n):

        if curr == 'right':
            if j+1 == n or visited.get((i,j+1)) :
                curr = 'down'
                continue
            j += 1
            count += 1
            res[i][j] = count
            visited[(i,j)] = 1




        if curr == 'down':
            if i+1 == n or visited.get((i+1,j)) :
                curr = 'left'
                continue
            i += 1
            count += 1
            res[i][j] = count
            visited[(i,j)] = 1


        if curr == 'left':
            if j-1 == -1 or visited.get((i,j-1)) :
                curr = 'up'
                continue
            j -= 1
            count += 1
            res[i][j] = count
            visited[(i,j)] = 1

        if curr == 'up':
            if i-1 == -1 or visited.get((i-1,j)) :
                curr = 'right'
                continue

            i -= 1
            count += 1
            res[i][j] = count
            visited[(i,j)] = 1

        if count == n*n:
            break

    return res
