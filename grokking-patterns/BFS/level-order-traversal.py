'''
Problem Statement #
Given a binary tree, populate an array to represent its level-by-level traversal. You should populate the values of all nodes of each level from left to right in separate sub-arrays.

Example 1:

  1
  2
  3
  4
  5
  6
  7
 Level Order Traversal:
 [[1],[2,3],[4,5,6,7]]
Example 2:

  12
  7
  1
  9
  10
  5
 Level Order Traversal:
 [[12],[7,1],[9,10,5]]
'''
class Node:
    def __init__(self,val):
        self.val = val
        self.left,self.right = None,None

head = Node(12)
head.left = Node(7)
head.right = Node(1)
head.left.left = Node(9)
head.right.left = Node(10)
head.right.right = Node(5)

import collections
def traverse(head):
    result = [[head.val]]
    q = collections.deque()
    q.append(head)
    def bfs(toDeque):
        if len(toDeque) <= 0:
            return
        level = []
        new_q = collections.deque()
        while len(toDeque):
            curr = toDeque.popleft()
            if curr.left:
                level.append(curr.left.val)
                new_q.append(curr.left)
            if curr.right:
                level.append(curr.right.val)
                new_q.append(curr.right)
        if len(level):
            result.append(level)
        bfs(new_q)
        return result
    return bfs(q)

print(traverse(head))

'''
Problem Statement #
Given a binary tree, populate an array to represent its level-by-level traversal in reverse order, i.e., the lowest level comes first. You should populate the values of all nodes in each level from left to right in separate sub-arrays.

Example 1:

  1
  2
  3
  4
  5
  6
  7
 [[4,5,6,7],[2,3],[1]]
 Reverse Level Order Traversal:
Example 2:

  12
  7
  1
  9
  10
  5
 [[9,10,5],[7,1],[12]]
 Reverse Level Order Traversal:
'''
def traverseReversed(head):
    result = collections.deque([head.val])
    q = collections.deque()
    q.append(head)
    def bfs(toDeque):
        if len(toDeque) <= 0:
            return
        level = []
        new_q = collections.deque()
        while len(toDeque):
            curr = toDeque.popleft()
            if curr.left:
                level.append(curr.left.val)
                new_q.append(curr.left)
            if curr.right:
                level.append(curr.right.val)
                new_q.append(curr.right)
        if len(level):
            result.appendleft(level)
        bfs(new_q)
        return result
    return bfs(q)

print(traverseReversed(head))
'''
Problem Statement #
Given a binary tree, populate an array to represent its zigzag level order traversal. You should populate the values of all nodes of the first level from left to right, then right to left for the next level and keep alternating in the same manner for the following levels.

Example 1:

 Zigzag Level Order Traversal:
 [[1],[3, 2],[4, 5, 6, 7]]
  1
  2
  3
  4
  5
  6
  7
Example 2:

  12
  7
  1
  9
  10
  5
  20
  17
 [[12],[1,7],[9,10,5][17,20]]
 Zigzag Level Order Traversal:
'''
def traverseZigZag(head):
    result = collections.deque()
    result.append([head.val])
    q = collections.deque()
    q.append(head)
    right,left = True,False
    currDir = right
    def bfs(currDir,toDeque):
        if len(toDeque) <= 0:
            return
        level = collections.deque()
        new_q = collections.deque()
        while len(toDeque):
            curr = toDeque.popleft()
            if curr.left:
                level.append(curr.left.val)
                new_q.append(curr.left)
            if curr.right:
                level.append(curr.right.val)
                new_q.append(curr.right)
        if len(level):
            if currDir == right:
                level.reverse()
            result.append(level)
            currDir = not currDir
        bfs(currDir,new_q)
        return result
    return bfs(currDir, q)

print(traverseZigZag(head))
